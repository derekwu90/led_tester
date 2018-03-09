""" the main function for led tester which could implement from the command prompt."""
import sys
import click
from . import parsefile
from . import lightgrid

click.disable_unicode_literals_warning = True



def creategrid(N, instructions):
    #initialize the light grid
    instanceLightGrid = lightgrid.LightGrid(N)
    
    for ins in instructions:
        #print(instanceLightGrid.check_cmd(ins))
        cmd,coo =instanceLightGrid.check_cmd(ins)
        instanceLightGrid.apply(cmd,coo)
    return instanceLightGrid

@click.command()
@click.option("--input", default=None, help="input URI(file or URL)")
def main(input=None):
    "Console script for led_tester."
    print("input",input)
    
    N,instructions = parsefile.parsefile(input)
    
    singleGrid = creategrid(N,instructions)
    
    print('#occupied:', singleGrid.count())
    
    return 0
    

if __name__=="__main__":
    sys.exit(main())