from ShootABall.ball import Ball
import pygame


def main():
    pygame.init()
    win = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    run = True
    ball = Ball(100, (500, 500), pygame.font.SysFont('comicsansms', 30))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                ball.click()

        win.fill((51, 51, 51))
        ball.draw(win)
        pygame.display.flip()


if __name__ == '__main__':
    main()
