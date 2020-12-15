import re 
import sys
with open(sys.argv[1], 'r') as f:
    lines = [line.rstrip() for line in f]

ans = 0
for li in lines:
    x = li.replace('-',' ')
    y = x.replace(':', '').split()    
    lowerBound = int(y[0])
    upperBound = int(y[1])
    checkChar = y[2]
    checkString = y[3]
    count = 0
    for char in checkString:
        if checkChar == char:
            count += 1
    if count >= lowerBound and count <= upperBound:
        ans += 1

print(ans)
    
    

    
        
    
