N=int(input())
A=list(map(int,input().split()))
print("YES" if sum(A)%2==0 else "NO")