N=int(input())
A=list(map(int,input().split()))
X=int(input())
div=X//sum(A)
mod=X%sum(A)
count,total=0,0
for a in A:
    count+=1
    total+=a
    if total>mod:
        break
print(len(A)*div+count)