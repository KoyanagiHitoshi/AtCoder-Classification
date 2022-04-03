L,R,d=map(int,input().split())
count=0
for num in range(L,R+1):
    if num%d==0:
        count+=1
print(count)