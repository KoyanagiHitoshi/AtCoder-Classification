A=[list(map(int,input().split())) for i in range(3)]
N=int(input())
B=[int(input()) for i in range(N)]
a=[[False]*3 for i in range(3)]
for i in range(3):
    for j in range(3):
        for b in B:
            if A[i][j]==b:
                a[i][j]=True
bingo=False
for i in range(3):
    if a[i][0] and a[i][1] and a[i][2]:
        bingo=True
for j in range(3):
    if a[0][j] and a[1][j] and a[2][j]:
        bingo=True
if a[0][0] and a[1][1] and a[2][2]:
    bingo=True
if a[2][0] and a[1][1] and a[2][0]:
    bingo=True
print("Yes" if bingo else "No")