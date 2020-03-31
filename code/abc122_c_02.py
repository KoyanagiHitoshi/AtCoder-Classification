N,Q=map(int,input().split())
S=input()
count=[0]*N
for i in range(1,N):
    count[i]+=count[i-1]
    if S[i-1:i+1]=="AC":count[i]+=1
for i in range(Q):
    l,r=map(int,input().split())
    print(count[r-1]-count[l-1])