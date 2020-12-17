import sys
with open(sys.argv[1], 'r') as f:
    lines = [line.rstrip() for line in f]

ans = 0
it = 0
for li in lines[1:]:
    it += 3
    if(li[it%31]) == '#':
        ans += 1
print(ans)