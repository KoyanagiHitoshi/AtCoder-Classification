n=int(input())
count=0
for i in range(2,n):
    count+=all(i%j for j in range(2,int(i**.5)+1))
print(count)