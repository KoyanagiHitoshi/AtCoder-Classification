N=int(input())
num=[]
for i in range(1,10**6):
    num.append(int(str(i)+str(i)))
num.sort()
count=0
for i in range(10**6-1):
    if num[i]<=N:
        count+=1
print(count)