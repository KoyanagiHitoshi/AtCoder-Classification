N=int(input())
A=list(map(int,input().split()))
count=[0]*N
for a in A:
    count[a-1]+=1
combination=0
for i in range(N):
    combination+=count[i]*(count[i]-1)//2
for a in A:
    print(combination-(count[a-1]-1))