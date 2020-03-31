n=int(input())
M=0
for i in range(n):
    a,b=map(int,input().split())
    M=max(M,a+b)
print(M)