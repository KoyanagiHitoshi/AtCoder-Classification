N=int(input())
count=0
for i in range(N):
    D1,D2=map(int,input().split())
    if D1==D2:
        count+=1
        if count>=3:
            print("Yes")
            exit()
    else:
        count=0
else:
    print("No")