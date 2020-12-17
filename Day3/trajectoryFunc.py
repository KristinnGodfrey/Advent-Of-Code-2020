import sys
with open(sys.argv[1], 'r') as f:
    lines = [line.rstrip() for line in f]

def slopes(start,shift,step):
    ans = 0
    idx = 0
    for li in lines[start::step]:
        idx += shift
        if(li[idx%31]) == '#':
            ans += 1
    return ans

a = slopes(1,1,1)
b = slopes(1,3,1)
c = slopes(1,5,1)
d = slopes(1,7,1)
e = slopes(2,1,2)

print(a*b*c*d*e)