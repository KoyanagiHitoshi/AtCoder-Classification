N,K=map(int,input().split())
D=set(input())
while sum(i in D for i in str(N))>0:
    N+=1
print(N)