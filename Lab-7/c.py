import pygame 
pygame.init()
screen = pygame.display.set_mode((800,800))
cl = pygame.time.Clock()
screen.fill((255,255,255))
x = 400
y = 400
q = True
while q:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            q = False
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(255,0,0),center=(x,y),radius=25)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if y > 0:
            y -= 25
    if pressed[pygame.K_DOWN]: 
        if y < 799:
            y += 25
    if pressed[pygame.K_LEFT]: 
        if x > 0:
            x -= 25
    if pressed[pygame.K_RIGHT]:
        if x < 799:
            x += 25

    pygame.display.flip()
    cl.tick(60)
