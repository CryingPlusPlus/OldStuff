import pygame
import neat
import time
import os
import random
from pygame.locals import *

pygame.font.init()
# UI größe
WIN_WIDTH = 288 * 2
WIN_HEIGHT = 800

# Bilder
BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
             pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
             pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))

STAT_FONT = pygame.font.SysFont('comicsans', 50)


# ------------------------------------------------------------------------------------------------------------------

class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]
        self.acc_q = True

    def acc(self, score):

        if self.acc_q and (score + 1) % 10 == 0:
            self.vel -= 1
            self.acc_q = False
        if (score + 1) % 10 == 1:
            self.acc_q = True

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1  # tickcount = time... t in physik

        d = self.vel * self.tick_count + 1.5 * self.tick_count ** 2  # physics bewegungsgleichung

        if d >= abs(self.vel) + 6:
            d = abs(self.vel) + 6

        # if d < 0:
        #    d -= 2

        self.y = self.y + d

        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > - 90:
                self.tilt -= self.ROT_VEL

    def draw(self, win):
        self.img_count += 1

        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME * 2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME * 3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME * 4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME * 4 + 1:  # animiert die flügel von dem vogel
            self.img = self.IMGS[0]
            self.img_count = 0

        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME * 2

        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft=(round(self.x), round(self.y))).center)
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)


class Pipe:
    GAP = 200
    VEL = 10

    def __init__(self, x, vel):
        self.x = x
        self.height = 0

        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True)
        self.PIPE_BOTTOM = PIPE_IMG
        self.VEL = vel
        self.passed = False
        self.set_height()
        self.acc_q = True

    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.VEL

    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)

        if t_point or b_point:
            return True
        else:
            return False

    def acc(self, score):

        if self.acc_q and (score + 1) % 10 == 0:
            self.VEL += 1
            self.acc_q = False
        if (score + 1) % 10 == 1:
            self.acc_q = True


class Base:
    VEL = 10
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH
        self.acc_q = True

    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH
        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))

    def acc(self, score):

        if self.acc_q and (score + 1) % 10 == 0:
            self.VEL += 1
            self.acc_q = False
        if (score + 1) % 10 == 1:
            self.acc_q = True


# -----------------------------------------------------------------------
def best_genome(genomes):
    best = None
    for _, g in genomes:
        if best is None:
            best = g
        elif g.fitness > best.fitness:
            best = g
    return best


ev = 0
best_g = None


def main(genomes, config):
    rem = []
    global ev
    ev += 1
    nets = []
    ge = []
    birds = []
    # neat stuff
    global best_g
    for x, (_, g) in enumerate(genomes):
        if best_g is not None and x == 0:
            g = best_g
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird(230, 350))
        g.fitness = 0
        ge.append(g)

    base = Base(730)
    pipes = [Pipe(600, 10)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    run = True

    score = 0

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        pipe_ind = 0

        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_ind = 1
        else:
            run = False
            break

        for x, bird in enumerate(birds):
            bird.move()
            bird.acc(score)
            #ge[x].fitness += 0.1

            output = nets[x].activate(
                (bird.y, abs(bird.y - pipes[pipe_ind].height), abs(bird.y - pipes[pipe_ind].bottom), bird.vel,
                 pipes[0].VEL))
            if output[0] > 0.5:
                bird.jump()

        base.move()
        add_Pipe = False
        for pipe in pipes:
            pipe.acc(score)
            for x, bird in enumerate(birds):
                if pipe.collide(bird):
                    ge[x].fitness -= 1
                    birds.pop(x)
                    nets.pop(x)
                    ge.pop(x)

                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_Pipe = True

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

            pipe.move()

        if add_Pipe:
            score += 1
            for g in ge:
                g.fitness += 1

            pipes.append(Pipe(600, (10 + score // 10)))

        for r in rem:
            pipes.remove(r)
            rem.remove(r)
            continue
        # bird.move()
        for x, bird in enumerate(birds):
            if bird.y + bird.img.get_height() > 730 or bird.y < 0:
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)
        base.acc(score)
        draw_window(win, birds, pipes, base, score)

    m_g = best_genome(genomes)
    if best_g is not None:
        if best_g.fitness < m_g.fitness:
            best_g = m_g
    else:
        best_g = m_g
    print('Ev: ', ev, 'Sc: ', score, 'Best Bird: ', m_g.fitness)
    best_g.fitness = 0


def draw_window(win, birds, pipes, base, score):
    win.blit(BG_IMG, (0, 0))
    for pipe in pipes:
        pipe.draw(win)
    base.draw(win)
    for bird in birds:
        bird.draw(win)

    text = STAT_FONT.render('Score: ' + str(score), 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    pygame.display.update()


def run(config_path):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet,
                         neat.DefaultStagnation, config_path)

    p = neat.Population(config)

    # p.add_reporter(neat.StdOutReporter(True))
    # stats = neat.StatisticsReporter
    # p.add_reporter(stats)

    winner = p.run(main, 50)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'NEAT_Config.txt')
    run(config_path)
