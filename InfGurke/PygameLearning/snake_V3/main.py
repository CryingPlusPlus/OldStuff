import pygame
import sys
from snake_V3.apple import Apple
from snake_V3.snake import Snake


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
        snake.move(apple=apple, win=win, r=r)
        apple.draw(win)
        pygame.display.update()
    pygame.quit()
    # return main()


if __name__ == '__main__':
    main()
