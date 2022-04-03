N=int(input())
A=list(map(int,input().split()))
element=[0]*(10**5)
total=sum(A)
for a in A:
    element[a-1]+=1
Q=int(input())
for q in range(Q):
    B,C=map(int,input().split())
    total+=element[B-1]*(C-B)
    if element[B-1]!=0:
        element[C-1]+=element[B-1]
        element[B-1]=0
    print(total)