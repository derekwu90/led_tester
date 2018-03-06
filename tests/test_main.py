from test_parsefile import *

from test_lightclass import *


def main():
    L1=LightTester(sizeGrid)
    for i in cmd:
        print(i)
        L1.apply(i)
        print(L1.count())
    


if __name__ == "__main__":
    main()

        
    