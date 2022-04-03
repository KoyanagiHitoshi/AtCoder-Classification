N=int(input())
S=list(map(int,input().split()))
T=list(map(int,input().split()))
for i in range(2*(N-1)):
    T[(i+1)%N]=min(T[(i+1)%N],T[i%N]+S[i%N])
for t in T:
    print(t)