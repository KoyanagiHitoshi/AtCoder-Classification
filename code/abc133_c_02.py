L,R=map(int,input().split())
left,right=L%2019,R%2019
minimum=2018**2
if R-L>=2019:
    minimum=0
else:
    for i in range(left,right+1):
        for j in range(i+1,right+1):
            minimum=min(minimum,i*j%2019)
print(minimum)