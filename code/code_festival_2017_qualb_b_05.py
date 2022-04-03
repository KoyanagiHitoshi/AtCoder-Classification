N=int(input())
D=sorted(map(int,input().split()))[::-1]
M=int(input())
T=sorted(map(int,input().split()))
for t in T:
    d=0
    while D and d!=t:
        d=D.pop()
    if d!=t:
        print("NO")
        break
else:
    print("YES")