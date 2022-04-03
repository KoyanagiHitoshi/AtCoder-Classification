D=list(map(int,input().split()))
J=list(map(int,input().split()))
weight=0
day=7
for i in range(1<<day):
    mining=0
    for j in range(day):
        if (i>>j)&1:
            mining+=D[j]
        else:
            mining+=J[j]
    weight=max(weight,mining)
print(weight)