H,W=map(int,input().split())
S=[input().split() for i in range(H)]
for h in range(H):
    for w in range(W):
        if S[h][w]=="snuke":
            print(chr(w+65)+str(h+1))