N=int(input())
AB=[]
takahashi=0
aoki=0
for i in range(N):
    a,b=map(int,input().split())
    AB.append([a,b,a+b])
AB.sort(key=lambda AB:(AB[2],AB[1],AB[0]),reverse=True)
for i in range(N):
    if i%2==0:
        takahashi+=AB[i][0]
    else:
        aoki+=AB[i][1]
print(takahashi-aoki)