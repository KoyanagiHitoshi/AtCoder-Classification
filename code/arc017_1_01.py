N=int(input())
print("YES" if all([N%n!=0 for n in range(2,N)]) else "NO")