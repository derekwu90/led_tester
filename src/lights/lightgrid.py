import numpy as np
import cmd

class LightGrid:
    """ class of light grid """
    def __init__(self, n):
        self.__gridsize = n
        self.__lightGrid = np.zeros((n,n),dtype=np.bool)
        
    def apply(self,cmd,coo):
        if(coo==None):
            pass
        else:
            #print(cmd,coo)
            if cmd=="turn on":
                self.__lightGrid[coo[0]:coo[1]+1,coo[2]:coo[3]+1]=True
            elif cmd=="turn off":
                self.__lightGrid[coo[0]:coo[1]+1,coo[2]:coo[3]+1]=False
            elif cmd =="switch":
                self.__lightGrid[coo[0]:coo[1]+1,coo[2]:coo[3]+1]=np.invert(self.__lightGrid[coo[0]:coo[1]+1,coo[2]:coo[3]+1])
    
    def count(self):
        return np.sum(self.__lightGrid)
    
    def check_cmd(self,cmd):
        minxindex = np.minimum(cmd[1][0],cmd[2][0])
        maxxindex = np.maximum(cmd[1][0],cmd[2][0])
        minyindex = np.minimum(cmd[1][1],cmd[2][1])
        maxyindex = np.maximum(cmd[1][1],cmd[2][1])
        
        if(maxxindex<0) or (minxindex >= self.__gridsize) or (minyindex >= self.__gridsize) or (maxyindex < 0):
            #print("Coordinate out of range")
            return cmd[0], None
        else:
            lightOrdered = [minxindex,maxxindex,minyindex,maxyindex]
            lightNegativeCorrected = [ 0 if i < 0 else i for i in lightOrdered]
            lightOutrangeCorrected = [self.__gridsize if i >= self.__gridsize else i for i in lightNegativeCorrected]
            #print(lightOrdered)
            #print(lightOutrangeCorrected)
            return cmd[0],lightOutrangeCorrected
            
            
        
        
        
                        
        