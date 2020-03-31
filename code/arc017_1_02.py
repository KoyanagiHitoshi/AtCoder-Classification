N=int(input())
print("NO" if any([N%n==0 for n in range(2,N)]) else "YES")