def f(k):
    N=str(k)
    return sum(int(N[-n-1])*(k**n) for n in range(len(N)))

A=int(input())
for k in range(10,10**4+1):
    if f(k)==A:
        print(k)
        break
else:
    print(-1)