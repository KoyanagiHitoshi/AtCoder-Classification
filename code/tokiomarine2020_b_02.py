A,V=map(int,input().split())
B,W=map(int,input().split())
T=int(input())
print("NO" if V==W or V<W or abs(A-B)/(V-W)>T else "YES")