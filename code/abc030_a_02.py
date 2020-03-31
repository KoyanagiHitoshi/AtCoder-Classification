a,b,c,d=map(int,input().split())
T,A=b/a,d/c
print("TAKAHASHI" if T>A else "AOKI" if T<A else "DRAW")