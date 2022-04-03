H,W=map(int,input().split())
A=[input() for h in range(H)]
count=0
for a in A:
    count+=a.count("#")
print("Possible" if H+W-1==count else "Impossible")