H,W=map(int,input().split())
S=[input().split() for i in range(H)]
columns="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for h in range(H):
    for w in range(W):
        if S[h][w]=="snuke":
            print(columns[w]+str(h+1))