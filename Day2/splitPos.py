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
    if checkString[lowerBound-1] == checkChar and checkString[upperBound-1] != checkChar:
        ans += 1        
    elif checkString[upperBound-1] == checkChar and checkString[lowerBound-1] != checkChar:
        ans += 1
print(ans)
    
    

    
        
    
