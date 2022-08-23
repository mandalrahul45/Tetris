import pygame

#matrix to represent each cell of the display(screen)
matrix = [[1,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [1,1,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,1,1,1,0,0,0,0,0,0],
          [0,0,0,0,0,0,1,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,1,0,0,0],
          [0,0,1,0,0,0,0,0,0,0,1,0,0,0],
          [0,0,1,0,0,0,0,0,0,0,1,0,0,0],
          [0,0,1,0,0,0,0,0,0,0,1,0,0,0],
          [0,0,1,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

#block settings (to be removed later):
rectSurf = pygame.Surface((40,40))
rectSurf.fill("Red")

#matrix to represent the 
def blitGrid(screen):
    for x in range(40,560,40):
        pygame.draw.rect(screen,"White",pygame.Rect(x,0,1,760))
    for y in range(40,760,40):
        pygame.draw.rect(screen,"White",pygame.Rect(0,y,560,1))

def updateMatrixToScreen(screen):
    for i in range(0,19):
        for j in range(0,14):
            if(matrix[i][j]==1):
                x=(40*j)
                y=(40*i)
                rectSurf.fill("Red")
                screen.blit(rectSurf,(x,y))