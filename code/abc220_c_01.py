N=int(input())
A=list(map(int,input().split()))
X=int(input())
div=X//sum(A)
mod=X%sum(A)
count=N*div
for a in A:
    count+=1
    mod-=a
    if mod<0:
        break
print(count)