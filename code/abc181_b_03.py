N=int(input())
count=[0]*(10**6+2)
for i in range(N):
    A,B=map(int,input().split())
    count[A]+=1
    count[B+1]-=1
for i in range(len(count)-1):
    count[i+1]+=count[i]
total=0
for i in range(len(count)):
    total+=count[i]*i
print(total)