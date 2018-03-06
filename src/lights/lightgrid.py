import numpy as np

class LightGrid:
    """ class of light grid """
    def __init__(self, n):
        self.__lightGrid = np.zeros((n,n),dtype=np.bool)
        
    def apply(self,cmd):
        if cmd[0]=="turn on":
            for i in range(cmd[1][0],cmd[2][0]+1):
                for j in range(cmd[1][1],cmd[2][1]+1):
                    self.__lightGrid[i][j]=True;
        elif cmd[0]=="turn off":
            for i in range(cmd[1][0],cmd[2][0]+1):
                for j in range(cmd[1][1],cmd[2][1]+1):
                    self.__lightGrid[i][j]=False;
        elif cmd[0]=="switch":
            for i in range(cmd[1][0],cmd[2][0]+1):
                for j in range(cmd[1][1],cmd[2][1]+1):
                    self.__lightGrid[i][j]=  not self.__lightGrid[i][j]
    
    def count(self):
        return np.sum(self.__lightGrid)