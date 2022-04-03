M,D=map(int,input().split())
count=0
for month in range(1,M+1):
    for day in range(1,D+1):
        d1=day%10
        d10=day//10
        if d1>=2 and d10>=2 and d1*d10==month:
            count+=1
print(count)