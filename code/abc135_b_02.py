N=int(input())
p=list(map(int,input().split()))
print("YES" if sum(1 for i in range(N) if p[i]!=i+1)<=2 else "NO")