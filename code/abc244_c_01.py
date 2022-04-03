N=int(input())
num=[i for i in range(2,2*N+2)]
print(1)
for i in range(N):
    num.remove(int(input()))
    print(num.pop())