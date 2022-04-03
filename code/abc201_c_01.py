S=input()
count=0
for i in range(10000):
    flag=[False]*10
    now=i
    for j in range(4):
        flag[now%10]=True
        now//=10
    flag2=True
    for j in range(10):
        if S[j]=='o' and not flag[j]:
            flag2=False
        if S[j]=='x' and flag[j]:
            flag2=False
    count+=flag2
print(count)