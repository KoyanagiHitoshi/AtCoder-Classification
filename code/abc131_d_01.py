N=int(input())
AB=[list(map(int,input().split())) for i in range(N)]
AB.sort(key=lambda x:x[1])
time=0
for i in range(N):
    time+=AB[i][0]
    if time>AB[i][1]:
        print("No")
        break
else:
    print("Yes")