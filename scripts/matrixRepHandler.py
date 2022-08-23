import pygame

blockCor=[3,5]
#matrix to represent each cell of the display(screen)
matrix = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

#block settings (to be removed later):
rectSurf = pygame.Surface((40,40))
rectSurf.fill("#FF7F50")

#matrix to represent the 
def blitGrid(screen):
    for x in range(40,560,40):
        pygame.draw.rect(screen,"White",pygame.Rect(x,0,1,760))
    for y in range(40,760,40):
        pygame.draw.rect(screen,"White",pygame.Rect(0,y,560,1))

def updateMatrixToScreen(screen):
    matrix[blockCor[0]][blockCor[1]] = 1
    
    for i in range(0,19):
        for j in range(0,14):
            if(matrix[i][j]==1):
                x=(40*j)
                y=(40*i)
                rectSurf.fill("#B22222")
                screen.blit(rectSurf,(x,y))
                
    matrix[blockCor[0]][blockCor[1]] = 0

def moveBlockInMatrix(dir):
    if(dir == "UP" and not blockCor[0]==0):
        blockCor[0]=blockCor[0]-1

    if(dir == "DOWN" and not blockCor[0]==18):
        blockCor[0]=blockCor[0]+1

    if(dir == "LEFT" and not blockCor[1]==0):
        blockCor[1]=blockCor[1]-1

    if(dir == "RIGHT" and not blockCor[1]==13):
        blockCor[1]=blockCor[1]+1
    