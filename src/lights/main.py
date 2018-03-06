""" the main function for led tester which could implement from the command prompt."""
import sys
import click
from parsefile import *
from lightgrid import *

click.disable_unicode_literals_warning = True

@click.command()
@click.option("--input", default=None, help="input URI(file or URL)")

def main(input=None):
    "Console script for led_tester."
    print("input",input)
    
    #get instructions from the file
    N,instructions = parsefile(input)
    
    #initialize the light grid
    exampleLightGrid = LightGrid(N)
    
    for cmd in instructions:
        #print(cmd)
        exampleLightGrid.apply(cmd)
    
    print('#occupied:', exampleLightGrid.count())
    
    return 0

if __name__=="__main__":
    sys.exit(main())