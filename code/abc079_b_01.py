N=int(input())
a,b=2,1
for i in range(N):
    a,b=b,a+b
print(a)