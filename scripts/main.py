import pygame
import sys
from Anime_Sub import subtitle
from matrixRepHandler import *
pygame.init()

#inititlized the screen and set caption:
WIDTH =560
HEIGHT=760
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tetris")  

 #initialized the clock:
clock = pygame.time.Clock()

#set the icon:
Icon = pygame.image.load("assets/images/Icon.png")
pygame.display.set_icon(Icon)

#game opening music:
pygame.mixer.music.load("assets/audio/omaewa.ogg")      
pygame.mixer.music.set_endevent(pygame.USEREVENT)
pygame.mixer.music.play() 

#to to play bgmusic :
playBgMusic = True

updateBlocksToMatrix()

#setting a timer to make the current block fall after every 500 ms
pygame.time.set_timer(pygame.USEREVENT+1,400)
#game runtime controller:
c= 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            # Pause button
    
       #if event.type == pygame.K_ESCAPE:

        #backgound music, plays after the opening music has ended
        if event.type == pygame.USEREVENT and playBgMusic:
            pygame.mixer.music.load("assets/audio/bgmusic.ogg")
            pygame.mixer.music.play(-1)
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or  event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                moveBlockInMatrix("UP")
                pygame.key.set_repeat()

            if event.key == pygame.K_a or  event.key == pygame.K_LEFT:
                moveBlockInMatrix("LEFT")
                pygame.key.set_repeat(150)

            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                moveBlockInMatrix("DOWN")
                pygame.key.set_repeat(150)

            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                moveBlockInMatrix("RIGHT")
                pygame.key.set_repeat(150)

            
            #automatic gravity( ;) ):
        if event.type == pygame.USEREVENT+1:
            moveBlockInMatrix("DOWN")

    #all game loop logic to be updated every frame goes here:
    screen.fill("black")
    blitGrid(screen)
    
    updateMatrixToScreen(screen)
    reachedBotton()
    printMat()
    print(blocksInMatrix[0].other_cordinates)
    if(c<800):
        subtitle(screen=screen,text="You are already Dead",test_time=20)
        c= c+1
    pygame.display.update()
    clock.tick(60)
    