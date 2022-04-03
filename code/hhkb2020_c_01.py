N=int(input())
p=list(map(int,input().split()))
checked=[False]*200001
num=0
for i in range(N):
    checked[p[i]]=True
    while checked[num]:
        num+=1
    print(num)