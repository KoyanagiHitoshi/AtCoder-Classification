N,M,X=map(int,input().split())
A=list(map(int,input().split()))
left=0
for a in A:
    if a>X:
        break
    left+=1
right=M-left
print(min(left,right))