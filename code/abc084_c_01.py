import math
csf=[map(int,input().split()) for i in range(int(input())-1)]
ans=[0]
for c,s,f in csf:
    ans=[math.ceil(max(0,x-s)/f)*f+s+c for x in ans]+[0]
[print(x) for x in ans]