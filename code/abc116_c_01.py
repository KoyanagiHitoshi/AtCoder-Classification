N=int(input())
H=list(map(int,input().split()))+[0]
ans=0
MIN=MAX=0
for i in range(N):
    if H[i]>H[i+1]:
        ans+=H[i]-MIN
        MIN=H[i+1]
    if i==N-1:
        print(ans)
        exit()