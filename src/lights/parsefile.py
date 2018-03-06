import re
import urllib.request

def checkurl(url):
    match = re.search(r'\s*http://.*txt',url)
    if match:
        req = urllib.request.Request(match.group())
        with urllib.request.urlopen(req) as open_file:
            lines = open_file.readlines()
    else:
        with open(url) as open_file:
            lines = open_file.readlines()
    return lines


def parsefile(url):
    
    lines = checkurl(url)
    # line1 store the size of grid.
    sizeGrid = int(lines[0])

    # get instruction from each line
    cmd=[]
    
    for line in lines[1:]:
        if not isinstance(line,str):
            line = line.decode()
        print(line)
        match = re.search('.*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*',line)
        if match:
            cmd.append([match.group(1),(int(match.group(2)),int(match.group(3))),(int(match.group(4)),int(match.group(5)))])
            
    return sizeGrid, cmd
