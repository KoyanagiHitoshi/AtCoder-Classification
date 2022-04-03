import bisect
N,M=map(int,input().split())
A=list(map(int,input().split()))
B=sorted(map(int,input().split()))
ans=10**9
for a in A:
    x=bisect.bisect_left(B,a)%M
    ans=min(ans,abs(B[x-1]-a),abs(B[x]-a))
print(ans)