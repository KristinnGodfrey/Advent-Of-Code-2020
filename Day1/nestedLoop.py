import sys
with open(sys.argv[1], 'r') as f:
    lines = [int(line.rstrip()) for line in f]

ans = 0
for li in lines:
    for i in lines:
        if(i != li and i+li==2020):
            ans = i*li            
print(ans)
            
