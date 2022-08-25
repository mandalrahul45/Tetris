import pygame
class Block:

    def __init__(self,mi,mj,color):
        #the vars mi,mj holds the cordinates of central single block in a group of block
        self.mi = mi
        self.mj = mj
        
        self.color=color

        #other_cordinates  list will be holding the coordinates of single blocks component to form a block
        #they will be set by the blocks implementing the block class
        self.other_cordinates = None #expected to have list of lists

class Iblock(Block):
     
    def __init__(self, mi, mj, color):
        super().__init__(mi, mj, color)
        self.updateOtherCordinates()
        self.updateLimits()
        

    def updateOtherCordinates(self):
        toc = [[self.mi,self.mj],
               [self.mi+1,self.mj],
               [self.mi+2,self.mj],
               [self.mi+3,self.mj]]
        self.other_cordinates=toc    
    
    def updateLimits(self):
        self.upLimit   =  self.other_cordinates[0][0]
        self.downLimit = self.other_cordinates[3][0]
        self.leftLimit = self.other_cordinates[0][1]
        self.rightLimit = self.other_cordinates[0][1]
    
    

