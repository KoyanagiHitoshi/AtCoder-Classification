N,M=map(int,input().split())
A=sorted(map(int,input().split()))[::-1]
B=sorted(map(int,input().split()))[::-1]
print("YES" if N>=M and all(a>=b for a,b in zip(A,B)) else "NO")