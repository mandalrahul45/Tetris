import pygame 
pygame.init()

import time

def subtitle(screen,text,test_time):
    text_font = pygame.font.Font("assets/Fonts/silk.ttf",20)
    text_surface = text_font.render(str(text), True, 'white')
    # text_surface.set_alpha(80)
    screen.blit(text_surface,text_surface.get_rect(midbottom = screen.get_rect().midbottom))