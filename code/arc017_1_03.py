N=int(input())
print("YES" if all([N%n for n in range(2,N)]) else "NO")