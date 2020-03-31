import fractions
A,B=map(int,input().split())
print(A*B//fractions.gcd(A,B))