N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
count=0
for i,b in enumerate(B):
    attack=min(b,A[i]+A[i+1])
    count+=attack
    A[i+1]-=max(0,attack-A[i])
print(count)