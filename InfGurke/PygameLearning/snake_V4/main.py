import pygame
from snake_V4.snake import Snake
from snake_V4.map import Map
import time
import gc

def main():
    gc.enable()
    pygame.init()
    win = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    snake = Snake((30, 30), 20, (15, 15))
    map = Map((30, 30), 20)
    run = True
    start = time.time()
    a = start
    initialrun = True
    while run:
        ms = clock.tick(120)
        pygame.display.set_caption("{}".format(len(snake.pos)))

        r = 4

        time.sleep(1/60)
        #b = time.time()
        fps = clock.get_fps()
        if fps > 0:
            newVel = 2 * 60 / fps
            #print(newVel)
            snake.updateVel(newVel)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYUP:
                keypressed = False
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    r = 3
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    r = 1
                if event.key == pygame.K_UP or event.key == ord('w'):
                    r = 0
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    r = 2
            else:
                r = 4
        win.fill((51, 51, 51))

        snake.move(win, r=r)

        #if initialrun:
        #    pygame.display.flip()
        #    initialrun = False
        #else:
        #    pygame.display.update(snake.getUpdate())
        pygame.display.flip()
        #a = b

    pygame.quit()


if __name__ == '__main__':
    main()
