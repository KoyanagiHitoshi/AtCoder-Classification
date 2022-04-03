n=int(input())
rabbit=[1,1]
for month in range(2,n+1):
    rabbit.append(rabbit[month-2]+rabbit[month-1])
print(rabbit[n])