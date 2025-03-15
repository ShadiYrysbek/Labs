import pygame 
pygame.init()
pygame.mixer.init()
songs = ['C:/Users/yrysb/Desktop/Labs/Lab-7/music/Krystal_Xu_-_Blue_Bird_From_Naruto_Shippuden_72249094.mp3',"C:/Users/yrysb/Desktop/Labs/Lab-7/music/Natan & Глюк'оZa - Улетай (zaycev.net) (4).mp3","C:/Users/yrysb/Desktop/Labs/Lab-7/music/Макс Корж - Малиновый закат (zaycev.net).mp3","C:/Users/yrysb/Desktop/Labs/Lab-7/music/МУЗЫКА В МАШИНУ - ГДЕ-ТО ТАМ (zaycev.net) (1).mp3"]


i = 0
pygame.mixer.music.load(songs[i%len(songs)])


screen = pygame.display.set_mode((1250,50))
pygame.display.set_caption("My music")


q = True
while q:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            q = False
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                i += 1
                i = i%len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()


            elif event.key == pygame.K_LEFT:
                i -= 1
                i = i%len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()


            elif event.key == pygame.K_UP:
                if i == 0:
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.unpause()


            elif event.key == pygame.K_DOWN:
                pygame.mixer.music.pause()

pygame.quit()



    