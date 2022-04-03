H,W,K=map(int,input().split())
c=[list(input()) for i in range(H)]
count=0
for bit_h in range(1<<H):
    for bit_w in range(1<<W):
        black=0
        for shift_h in range(H):
            for shift_w in range(W):
                if c[shift_h][shift_w]=="#" and (bit_h>>shift_h)&1 and (bit_w>>shift_w)&1:
                    black+=1
        if black==K:
            count+=1
print(count)