from snake_neat_V2.snake import Snake
import pygame
import sys
from snake_neat_V2.apple import Apple


def main():
    pygame.init()
    win = pygame.display.set_mode((600, 600))
    snake = Snake((15, 15), (30, 30), 20)
    apple = Apple(5, 15, 20, 30, 30, snake)
    run = True
    clock = pygame.time.Clock()
    while run:
        r = 4
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
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
        apple.draw(win)
        snake.move(apple=apple, r=r)
        snake.draw(win)
        snake.disconnectCells(win)
        snake.connectCells(win)
        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
