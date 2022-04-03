N=int(input())
AB=[list(map(int,input().split())) for i in range(N)][::-1]
count=0
for i in range(N):
    AB[i][0]+=count
    if AB[i][0]%AB[i][1]!=0:
        count+=AB[i][1]-(AB[i][0]%AB[i][1])
print(count)