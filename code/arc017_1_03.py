N=int(input())
print("NO" if any(N%num==0 for num in range(2,N)) else "YES")