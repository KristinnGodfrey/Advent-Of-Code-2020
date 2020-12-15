import sys
with open(sys.argv[1], 'r') as f:
    lines = [int(line.rstrip()) for line in f]

ans = 0
for li in lines:
    for i in lines:
        for i2 in lines:
            if(i+li+i2==2020):
              ans = i*li*i2            
print(ans)
