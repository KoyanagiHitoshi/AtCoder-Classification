N=int(input())
v=set(range(N+1))
for i in range(N-1):
    v&=set(map(int,input().split()))
print("Yes" if v else "No")