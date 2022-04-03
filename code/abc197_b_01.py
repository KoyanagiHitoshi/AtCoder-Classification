H,W,X,Y=map(int,input().split())
S=[input() for i in range(H)]
di=[1,0,-1,0]
dj=[0,1,0,-1]
X-=1
Y-=1
count=1
for d in range(4):
    ni,nj=X,Y
    while True:
        ni+=di[d]
        nj+=dj[d]
        if ni<0 or ni>=H or nj<0 or nj>=W:
            break
        if S[ni][nj]=="#":
            break
        count+=1
print(count)