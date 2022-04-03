N=int(input())
A=list(map(int,input().split()))
count=[0]*(10**5)
total=sum(A)
for a in A:
    count[a-1]+=1
Q=int(input())
for q in range(Q):
    B,C=map(int,input().split())
    total+=count[B-1]*(C-B)
    if count[B-1]!=0:
        count[C-1]+=count[B-1]
        count[B-1]=0
    print(total)