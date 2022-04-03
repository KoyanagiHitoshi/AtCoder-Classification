N=int(input())
SP=[]
for i in range(N):
    s,p=input().split()
    SP.append([s,int(p)])
SP.sort(key=lambda x:x[1])
trans_SP=list(zip(*SP))
print(trans_SP[0][-1] if trans_SP[1][-1]>sum(trans_SP[1])/2 else "atcoder")