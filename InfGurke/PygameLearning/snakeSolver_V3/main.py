import pygame
from snakeSolver_V3.snake import Snake


def main():
    pygame.init()
    win = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    run = True
    snake = Snake()

    while run:
        #clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        win.fill((51, 51, 51))
        snake.move(win)
        pygame.display.flip()
        if not snake.alive:
            break
    return len(snake.pos)


def test(an):
    sum = 0
    n = 0
    for i in range(an):
        print(i)
        sum += main()
        n += 1
    print(n)
    print(sum / n)
if __name__ == '__main__':
    test(10)
