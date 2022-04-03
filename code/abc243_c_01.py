N=int(input())
XY=[list(map(int,input().split())) for i in range(N)]
S=input()
for i in range(N):
    XY[i].append(S[i])
XY.sort(key=lambda x:(x[1],x[0]))
for i in range(N-1):
    if XY[i][1]==XY[i+1][1] and XY[i][2]=="R" and XY[i+1][2]=="L":
        print("Yes")
        break
else:
    print("No")