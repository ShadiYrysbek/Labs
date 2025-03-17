#крестики нолики v1.0
import pygame
pygame.init()
screen = pygame.display.set_mode((900,900))
cl = pygame.time.Clock()
screen.fill((255,255,255))
pygame.draw.line(screen,(255,0,0),(0,300),(900,300))
pygame.draw.line(screen,(255,0,0),(0,600),(900,600))
pygame.draw.line(screen,(255,0,0),(300,0),(300,900))
pygame.draw.line(screen,(255,0,0),(600,0),(600,900))
q = True 
i = 0
q1,q2,q3,q4,q5,q6,q7,q8,q9 = True,True,True,True,True,True,True,True,True
a = [[0,0,0],
     [0,0,0],
     [0,0,0]]
while q:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            q = False
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_KP1] and q1:
        x = 150
        y = 750
        i+=1
        if i%2==1:
            pygame.draw.circle(screen,(255,0,0),(x,y),120)
            a[2][0]=1
        else:
            pygame.draw.circle(screen,(0,0,0),(x,y),120)
            a[2][0]=2
        q1 = False

    elif pressed[pygame.K_KP4] and q4:
        x  = 150
        y = 450
        i+=1
        if i%2==1:
            pygame.draw.circle(screen,(255,0,0),(x,y),120)
            a[1][0]=1
        else:
            pygame.draw.circle(screen,(0,0,0),(x,y),120)
            a[1][0]=2
        q4 = False
    elif pressed[pygame.K_KP7] and q7:
        x  = 150
        y = 150
        i+=1
        if i%2==1:
            pygame.draw.circle(screen,(255,0,0),(x,y),120)
            a[0][0]=1
        else:
            pygame.draw.circle(screen,(0,0,0),(x,y),120)
            a[0][0]=2
        q7 = False
    elif pressed[pygame.K_KP8] and q8:
        x  = 450
        y = 150
        i+=1
        if i%2==1:
            pygame.draw.circle(screen,(255,0,0),(x,y),120)
            a[0][1]=1
        else:
            pygame.draw.circle(screen,(0,0,0),(x,y),120)
            a[0][1]=2
        q8 = False
    elif pressed[pygame.K_KP2] and q2:
        x  = 450
        y = 750
        i+=1
        if i%2==1:
            pygame.draw.circle(screen,(255,0,0),(x,y),120)
            a[2][1]=1
        else:
            pygame.draw.circle(screen,(0,0,0),(x,y),120)
            a[2][1]=2
        q2 = False
    elif pressed[pygame.K_KP5] and q5:
        x  = 450
        y = 450
        i+=1
        if i%2==1:
            pygame.draw.circle(screen,(255,0,0),(x,y),120)
            a[1][1]=1
        else:
            pygame.draw.circle(screen,(0,0,0),(x,y),120)
            a[1][1]=2
        q5 = False
    elif pressed[pygame.K_KP9] and q9:
        x  = 750
        y = 150
        i+=1
        if i%2==1:
            pygame.draw.circle(screen,(255,0,0),(x,y),120)
            a[0][2]=1
        else:
            pygame.draw.circle(screen,(0,0,0),(x,y),120)
            a[0][2]=2
        q9 = False
    elif pressed[pygame.K_KP6] and q6:
        x  = 750
        y = 450
        i+=1
        if i%2==1:
            pygame.draw.circle(screen,(255,0,0),(x,y),120)
            a[1][2]=1
        else:
            pygame.draw.circle(screen,(0,0,0),(x,y),120)
            a[1][2]=2
        q6 = False
    elif pressed[pygame.K_KP3] and q3:
        x  = 750
        y = 750
        i+=1
        if i%2==1:
            pygame.draw.circle(screen,(255,0,0),(x,y),120)
            a[2][2]=1
        else:
            pygame.draw.circle(screen,(0,0,0),(x,y),120)
            a[2][2]=2
        q3 = False
    # elif (q1 or q2 or q3 or q4 or q5 or q6 or q7 or q8 or q9) == False:
    #     screen.fill((255,255,255))
    #     pygame.draw.line(screen,(255,0,0),(0,300),(900,300))
    #     pygame.draw.line(screen,(255,0,0),(0,600),(900,600))
    #     pygame.draw.line(screen,(255,0,0),(300,0),(300,900))
    #     pygame.draw.line(screen,(255,0,0),(600,0),(600,900))
    #     q1,q2,q3,q4,q5,q6,q7,q8,q9 = True,True,True,True,True,True,True,True,True
          


    elif pressed[pygame.K_SPACE]:
        screen.fill((255,255,255))
        pygame.draw.line(screen,(255,0,0),(0,300),(900,300))
        pygame.draw.line(screen,(255,0,0),(0,600),(900,600))
        pygame.draw.line(screen,(255,0,0),(300,0),(300,900))
        pygame.draw.line(screen,(255,0,0),(600,0),(600,900))
        q1,q2,q3,q4,q5,q6,q7,q8,q9 = True,True,True,True,True,True,True,True,True
        a = [[0,0,0],
             [0,0,0],
             [0,0,0]]
    
    elif (a[0][0] == a[0][1] == a[0][2] == 1 or a[1][0] == a[1][1] == a[1][2] == 1 or a[2][0] == a[2][1] == a[2][2] == 1 or a[0][0] == a[1][0] == a[2][0] == 1 or a[0][1] == a[1][1] == a[2][1] == 1 or a[0][2] == a[1][2] == a[2][2] == 1 or a[0][0] == a[1][1] == a[2][2] == 1 or a[0][2] == a[1][1] == a[2][0] == 1):
        q1,q2,q3,q4,q5,q6,q7,q8,q9 = False,False,False,False,False,False,False,False,False


    elif (a[0][0] == a[0][1] == a[0][2] == 2 or a[1][0] == a[1][1] == a[1][2] == 2 or a[2][0] == a[2][1] == a[2][2] == 2 or a[0][0] == a[1][0] == a[2][0] == 2 or a[0][1] == a[1][1] == a[2][1] == 2 or a[0][2] == a[1][2] == a[2][2] == 2 or a[0][0] == a[1][1] == a[2][2] == 2 or a[0][2] == a[1][1] == a[2][0] == 2):
        q1,q2,q3,q4,q5,q6,q7,q8,q9 = False,False,False,False,False,False,False,False,False

    



    pygame.display.flip()
    cl.tick(60)

print(a)