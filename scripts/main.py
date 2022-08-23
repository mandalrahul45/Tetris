import pygame
import sys

pygame.init()

#inititlized the screen and set caption:
screen = pygame.display.set_mode((600,770))
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

#game runtime controller:
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #backgound music, plays after the opening music has ended
        if event.type == pygame.USEREVENT:
            pygame.mixer.music.load("assets/audio/bgmusic.ogg")
            pygame.mixer.music.play(-1)
    #all game loop logic to be updated every frame goes here:

    pygame.display.update()
    clock.tick(60)