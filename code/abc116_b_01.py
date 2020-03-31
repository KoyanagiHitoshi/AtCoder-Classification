S=int(input())
l=[0]*1000000
l[0]=0
l[1]=S
for i in range(2,1000000):
    if l[i-1]%2==0:
       l[i]=l[i-1]//2
    else:
        l[i]=3*l[i-1]+1
    for j in range(1,i-1):
        if l[i]==l[j]:
            print(i)
            exit()