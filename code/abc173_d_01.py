N=int(input())
A=list(map(int,input().split()))
total=0
A.sort(reverse=True)
insert=N-1
for i in range(N):
    add=2
    if i==0:
        add=1
    for j in range(add):
        if insert>0:
            total+=A[i]
            insert-=1
print(total)