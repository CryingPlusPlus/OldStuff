import pygame

#initialisiere pygame
pygame.init()

#fenster
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('First Game')

#player
x = 50
y = 50
width = 40
height = 60
vel = 5

run = True


#draw()
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        x -= vel
    if key[pygame.K_RIGHT]:
        x += vel
    if key[pygame.K_UP]:
        y -= vel
    if key[pygame.K_DOWN]:
        y += vel


    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
    win.fill((0, 0, 0))




pygame.quit()
