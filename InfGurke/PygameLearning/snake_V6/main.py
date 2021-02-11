import pygame
from snake_V6.snake import Snake


def main(highest):
    pygame.init()
    win = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    snake = Snake((30, 30))
    snake.alive = True
    run = True

    while run:
        pygame.display.set_caption("{}".format(len(snake.pos)))
        if highest < len(snake.pos):
            highest = len(snake.pos)
            print(highest)
        clock.tick(60)
        r = 4
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
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
        snake.move(win, r)
        pygame.display.flip()
        if not snake.alive:
            break
    return main(highest)


if __name__ == '__main__':
    main(0)
