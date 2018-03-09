import numpy as np

class LightTester:
    """ class of light grid """
    def __init__(self, n):
        self.__lightGrid = np.zeros((n,n),dtype=np.bool)
        
    def apply(self,cmd):
        minxindex = np.minimum(cmd[1][0],cmd[2][0])
        maxxindex = np.maximum(cmd[1][0],cmd[2][0])
        minyindex = np.minimum(cmd[1][1],cmd[2][1])
        maxyindex = np.maximum(cmd[1][1],cmd[2][1])
        if cmd[0]=="turn on":
            self.__lightGrid[minxindex:maxxindex+1,minyindex:maxyindex+1]=True;
        elif cmd[0]=="turn off":
            self.__lightGrid[minxindex:maxxindex+1,minyindex:maxyindex+1]=False;
        elif cmd[0]=="switch":
            self.__lightGrid[minxindex:maxxindex+1,minyindex:maxyindex+1]=np.invert(self.__lightGrid[minxindex:maxxindex+1,minyindex:maxyindex+1]);
    
    def count(self):
        return np.sum(self.__lightGrid)
            
 