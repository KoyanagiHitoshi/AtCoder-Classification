N,K=map(int,input().split())
if N%2!=0:N=N+1
print("YES" if N//2>=K else "NO")