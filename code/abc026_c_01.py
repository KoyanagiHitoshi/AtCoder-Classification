N=int(input())
B=[[1,[]] for i in range(N)]
for i in range(1,N):
    B[int(input())-1][1]+=[i]
for i in range(N-1,-1,-1):
    if B[i][1]:
        t=[B[j][0] for j in B[i][1]]
        B[i][0]=max(t)+min(t)+1
print(B[0][0])