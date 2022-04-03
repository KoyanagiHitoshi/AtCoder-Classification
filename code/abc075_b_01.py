H,W=map(int,input().split())
S=[input() for i in range(H)]
for i in range(H):
    line=""
    for j in range(W):
        if S[i][j]=="#":
            line+="#"
        else:
            line+=str(sum([t[max(0,j-1):min(W,j+2)].count("#") for t in S[max(0,i-1):min(H,i+2)]]))
    print(line)