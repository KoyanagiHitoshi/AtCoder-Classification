N=int(input())
print("Yes" if [4*x+7*y for y in range(101) for x in range(101)].count(N) else "No")