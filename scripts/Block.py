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
    
    #updateLimits sets or updates all the limits for all kinds of blocks which inherits this Block class
    def updateLimits(self):
        li,lj = 10e10,10e10
        mi,mj = -1,-1
        for cor in self.other_cordinates:
            li = min(li,cor[0])
            mi = max(mi,cor[0])

            lj = min(lj,cor[1])
            mj = max(mj,cor[1])

        self.upLimit    =   li
        self.downLimit  =   mi
        self.leftLimit  =   lj
        self.rightLimit =   mj
    
    # def canGoDown(self,blocksInMatrix):

    #     hasBlock=False
    #     for blk in blocksInMatrix[1:]:
    #         for otc in blk.other_cordinates:
    #             for otcOfSelf in self.other_cordinates:
    #                 if otcOfSelf[0]+1==otc[0] and otc[1] == otcOfSelf[1]:
    #                     hasBlock = True
    #                     break
        
    #     return(not self.downLimit==18 and not hasBlock)
    
    # def canGoRight(self,blocksInMatrix):

    #     hasBlock=False
    #     for blk in blocksInMatrix[1:]:
    #         for otc in blk.other_cordinates:
    #             for otcOfSelf in self.other_cordinates:
    #                 if otcOfSelf[1]+1==otc[1] and otc[0] == otcOfSelf[0]:
    #                     hasBlock = True
    #                     break
        
    #     return(not self.rightLimit==13 and not hasBlock)
    
    # def canGoLeft(self,blocksInMatrix):

    #     hasBlock=False
    #     for blk in blocksInMatrix[1:]:
    #         for otc in blk.other_cordinates:
    #             for otcOfSelf in self.other_cordinates:
    #                 if otcOfSelf[1]-1==otc[1] and otc[0] == otcOfSelf[0]:
    #                     hasBlock = True
    #                     break
        
    #     return(not self.leftLimit==0 and not hasBlock)
    

    #This method(canMoveTo) checks if the current_Block can move to a particular direction:
    def canMoveTo(self,dir,blocksInMatrix):

        hasABlockToLeft=False
        hasABlockToRight=False
        hasABlockToDown=False
        for blk in blocksInMatrix[1:]:
            for otc in blk.other_cordinates:
                for otcOfSelf in self.other_cordinates:

                    if dir == "LEFT" and otcOfSelf[1]-1==otc[1] and otc[0] == otcOfSelf[0]:
                        hasABlockToLeft = True

                    if dir == "RIGHT" and otcOfSelf[1]+1==otc[1] and otc[0] == otcOfSelf[0]:
                        hasABlockToRight = True

                    if dir == "DOWN" and otcOfSelf[0]+1==otc[0] and otc[1] == otcOfSelf[1]:
                        hasABlockToDown = True
        
        if dir == "LEFT":
            return(not self.leftLimit==0 and not hasABlockToLeft)

        elif dir == "RIGHT":
            return(not self.rightLimit==13 and not hasABlockToRight)
        
        elif dir == "DOWN":
            return(not self.downLimit==18 and not hasABlockToDown)


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
        self.updateLimits()
    

