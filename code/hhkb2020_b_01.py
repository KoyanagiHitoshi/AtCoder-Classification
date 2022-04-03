H,W=map(int,input().split())
S=[input() for i in range(H)]
ans=0
for h in range(H):
    for w in range(W):
        if S[h][w]==".":
            if w+1<W and S[h][w+1]==".":
                ans+=1
            if h+1<H and S[h+1][w]==".":
                ans+=1
print(ans)