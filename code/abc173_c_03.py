import itertools
H,W,K=map(int,input().split())
c=[list(input()) for i in range(H)]
count=0
for bit_h in itertools.product([0,1],repeat=H):
    for bit_w in itertools.product([0,1],repeat=W):
        black=0
        for h,w in itertools.product(range(H),range(W)):
            if c[h][w]=="#" and bit_h[h]&1 and bit_w[w]&1:
                black+=1
        if black==K:
            count+=1
print(count)