# create a feet to meter converter in pygame
# create a game that allows to show multiple instances of the same image on the screen
# create a game that allows to overlap music over each other


# def conv(a):
#     return (0.348*a)


# import pygame

# a = int(input())

# pygame.init()
# wind = pygame.display.set_mode((800, 800))
# clock = pygame.time.Clock()

# font = pygame.font.SysFont("Verdana", 60)
# game = font.render(str(conv(a)), True, (0,0,0))

# done = True
# while done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = False
    
#         wind.fill((255,255,255))
#         wind.blit(game, (200, 350))
#     pygame.display.flip()
#     clock.tick(60)  

# pygame.quit()




import pygame
import random

pygame.init()
wind = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

b = pygame.image.load("C:/Users/yrysb/Desktop/Labs/Lab-9/i (1).webp")
b = pygame.transform.scale(b, (30, 30))


done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                wind.blit(b,(random.randint(0,600),random.randint(0,600)))
    pygame.display.flip()
    clock.tick(60)  
pygame.quit()
