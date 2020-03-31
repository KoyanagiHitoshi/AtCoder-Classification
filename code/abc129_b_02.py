n=int(input())
w=list(map(int,input().split()))
m=max(w)
for i in range(n):
    m=min(m,abs(sum(w[:i+1])-sum(w[i+1:])))
print(m)