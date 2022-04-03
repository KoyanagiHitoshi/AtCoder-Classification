N,K=map(int,input().split())
A=set()
for i in range(K):
    input()
    A|=set(input().split())
print(N-len(A))