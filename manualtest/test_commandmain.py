""" console script for led tester."""
import sys
import click
from test_parsefun import *
from test_main import *

click.disable_unicode_literals_warning = True

@click.command()
@click.option("--input", default=None, help="input URI(file or URL)")

def main(input=None):
    "Console script for led_tester."
    print("input",input)
    
    N,instruction = parsefile(input)
    
    L1=LightTester(N)
    for cmd in instruction:
        print(cmd)
        L1.apply(cmd)
    
    print('#occupied:', L1.count())
    return 0

if __name__=="__main__":
    sys.exit(main())
  
    