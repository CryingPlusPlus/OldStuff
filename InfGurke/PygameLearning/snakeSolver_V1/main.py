from snakeSolver_V1.snake import Snake
from snakeSolver_V1.solver import Solver
import pygame


def main():
    pygame.init()
    win = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    run = True
    snake = Snake((15, 15), 20, (30, 30))
    solver = Solver(snake)
    while run:
        r = 4
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
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
        #if snake.current == 0:
        #    snake.lastcomp = solver.way[0]
        #    solver.way.pop(0)
        #if snake.apple.appleEaten:
        #    solver.way = solver.findWay()
        #    solver.formatWay()
        #    snake.apple.appleEaten = False
        snake.move(win, r)

        #solver.draw(win)
        #snake.draw(win)
        #snake.apple.draw(win)
        #solver.findWay()

        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()