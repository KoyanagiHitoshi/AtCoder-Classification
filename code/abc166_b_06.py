N,K=map(int,input().split())
A=set()
for k in range(K):
    d=input()
    A|=set(input().split())
print(N-len(A))