N,X=map(int,input().split())
moved=set([0])
for i in range(N):
    a,b=map(int,input().split())
    jump=set()
    for x in moved:
        jump.add(x+a)
        jump.add(x+b)
    moved=jump
print("Yes" if X in moved else "No")