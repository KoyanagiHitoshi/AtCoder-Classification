N=int(input())
K=list(map(int,input().split()))
K.append(K[-1])
K.insert(0,K[0])
L=[]
for i in range(N):
    L.append(min(K[i],K[i+1]))
print(*L)