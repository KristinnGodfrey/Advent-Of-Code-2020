import sys
with open(sys.argv[1], 'r') as f:
    lines = [int(line.rstrip()) for line in f]
    
for li in lines:
    for i in lines:
        if(i+li==2020):
            print(i*li)
            continue
