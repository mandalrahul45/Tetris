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

#backgound music:
bg_music = pygame.mixer.Sound("assets/audio/bgmusic.ogg")
bg_music.play(loops=-1)

#game runtime controller:
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #all game loop logic to be updated every frame goes here:

    pygame.display.update()
    clock.tick(60)