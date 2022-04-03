N=int(input())
print("YES" if all(N%num for num in range(2,N)) else "NO")