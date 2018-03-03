
# instructions are read from filename, N is the number of grids in the light board
def main(filename, N):
    
    #initilize the light board
    lights = LightTester(N)
    
    #parse the file from the filen with the filename
    instructions = parse_file(filename)
    
    #execute the cmd from the instructions
    
    for singleinstruction in instructions:
        lights.apply(singleinstruction)
        
    
    print("#occupied: ",lights.count())
    
    

class LightTester():
    """a class that represent the light boards, including all executions on the boards """
    __lights__= []
    __onlights__ =[]
    
    def __init__(self,N):
        #initialize the lights coordinates
        self.lights=[(x,y) for x in range(N) for y in range(N)]
    
    def apply(self,cmd):
        if cmd is "switch on":
            pass
        elif cmd is "switch off":
            pass
        else:
            pass
        
    def count(self):
        
        return count