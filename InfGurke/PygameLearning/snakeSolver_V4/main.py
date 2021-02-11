import pygame
from snakeSolver_V2.snake import Snake


def main():
    pygame.init()
    win = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    run = True
    snake = Snake()

    while run:
        pygame.display.set_caption("{}".format(len(snake.pos)))
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
    highest = 1
    lowest = 30*30+1
    for i in range(an):
        #print(i)
        l = main()
        sum += l
        n += 1

        if l > highest:
            highest = l
        if l < lowest:
            lowest = l
        print('n:', i, 'Arith:', sum / n, 'high', highest, 'low:', lowest)
if __name__ == '__main__':
    test(1000)
