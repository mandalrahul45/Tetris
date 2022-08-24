import pygame
from Block import *

current_Block=Iblock(0,1,"Red")

#this is to represent all the blocks in the matrix
#THE BLOCK AT 0th INDEX ALWAYS REPRESENT THE CURRENT BLOCK
blocksInMatrix=[current_Block]

#current_Block is set to None to better redability and understanding of code
current_Block=None

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

def initializeMatrix():
    for i in range(0,19):
        for j in range(0,14):
            matrix[i][j]=0


#block settings (to be removed later):
rectSurf = pygame.Surface((40,40))
rectSurf.fill("#FF7F50")

#to update the current_Block to the matrix:
def updateBlocksToMatrix():
    initializeMatrix()
    for blk in blocksInMatrix:
        for otc in blk.other_cordinates:
            matrix[otc[0]][otc[1]] = blk.color

def blitGrid(screen):
    for x in range(40,560,40):
        pygame.draw.rect(screen,"White",pygame.Rect(x,0,1,760))
    for y in range(40,760,40):
        pygame.draw.rect(screen,"White",pygame.Rect(0,y,560,1))

def updateMatrixToScreen(screen):
    for i in range(0,19):
        for j in range(0,14):
            if(not matrix[i][j] == 0):
                x=(40*j)
                y=(40*i)
                rectSurf.fill(matrix[i][j])
                screen.blit(rectSurf,(x,y))
                

def printMat():
    for i in range(0,19):
        for j in range(0,14):
            print(matrix[i][j]," ",end="")
        print()
    print()
    print()

#TO DO: to set the restrictions for limits
def moveBlockInMatrix(dir):
    if(dir == "UP" and not blocksInMatrix[0].mi==0):
        blocksInMatrix[0].mi=blocksInMatrix[0].mi-1

    if(dir == "DOWN" and not blocksInMatrix[0].mi==18):
        blocksInMatrix[0].mi=blocksInMatrix[0].mi+1

    if(dir == "LEFT" and not blocksInMatrix[0].mj==0):
        blocksInMatrix[0].mj=blocksInMatrix[0].mj-1

    if(dir == "RIGHT" and not blocksInMatrix[0].mj==13):
        blocksInMatrix[0].mj=blocksInMatrix[0].mj+1

    blocksInMatrix[0].updateOtherCordinates()
    updateBlocksToMatrix()
    