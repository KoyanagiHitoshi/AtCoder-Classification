N=int(input())
A=list(map(int,input().split()))
m=[0]*200
total=0
for a in A:
    mod=a%200
    total+=m[mod]
    m[mod]+=1
print(total)