import re
import urllib.request

with open("../data/test_data.txt") as open_file:
    lines = open_file.readlines()

# line1 store the size of grid.
sizeGrid = int(lines[0])

# get cmd from each line

cmd=[]

for str in lines[1:]:
    match = re.search('.*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*',str)
    if match:
        cmd.append([match.group(1),(int(match.group(2)),int(match.group(3))),(int(match.group(4)),int(match.group(5)))]);
    
#print(sizeGrid)
#print(type(sizeGrid))
#print(cmd)

#print(cmd[0][2])
    
#print(cmd[0][2][1]) 