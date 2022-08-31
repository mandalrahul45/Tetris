import random
from re import I
import pygame
from Block import *


def generateRandomBlock():
    blockNames = ['Iblock','Tblock']
    return(eval(f"{random.choice(blockNames)}(0,6)"))

current_Block=generateRandomBlock()

#this is to represent all the blocks in the matrix
#THE BLOCK AT 0th INDEX ALWAYS REPRESENT THE CURRENT BLOCK
blocksInMatrix=[current_Block]

# blocksInMatrix.append(Iblock(15,6,"#45B8AC"))

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


rectSurf = pygame.Surface((40,40))

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
            print(f"{matrix[i][j]:7}"," ",end="")
        print()
    print()
    print()

def moveBlockInMatrix(dir):
    # <<<<<<< VERY IMPORTANT >>>>>>>>>
    ## TO DO: CHECK IF THE ROTATION IS POSSIBLE 
    
    if(dir == "UP"): # The block rotation is done using the moveBlockInMatrix(..) in order to comply with other updations
        blocksInMatrix[0].rotateBlock()

    if(dir == "DOWN" and blocksInMatrix[0].canMoveTo(dir,blocksInMatrix)):
        blocksInMatrix[0].mi=blocksInMatrix[0].mi+1

    if(dir == "LEFT" and blocksInMatrix[0].canMoveTo(dir,blocksInMatrix)):
        blocksInMatrix[0].mj=blocksInMatrix[0].mj-1

    if(dir == "RIGHT" and blocksInMatrix[0].canMoveTo(dir,blocksInMatrix)):
        blocksInMatrix[0].mj=blocksInMatrix[0].mj+1

    blocksInMatrix[0].updateOtherCordinates()
    updateBlocksToMatrix()



def reachedBotton():
    '''This method checks if the current block (blocksInMatrix[0]) 
        has reached the bottom and spawns a new current block if so.'''

    if not blocksInMatrix[0].canMoveTo("DOWN",blocksInMatrix):
        blocksInMatrix.insert(0,generateRandomBlock())


