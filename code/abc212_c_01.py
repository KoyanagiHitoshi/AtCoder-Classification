import bisect
N,M=map(int,input().split())
A=list(map(int,input().split()))
B=sorted(map(int,input().split()))
ans=10**9
for a in A:
    x=bisect.bisect_left(B,a)-1
    if x!=M-1:
        ans=min(ans,abs(B[x]-a),abs(B[x+1]-a))
    else:
        ans=min(ans,abs(B[x]-a))
print(ans)