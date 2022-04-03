N=int(input())
count=[0]*(10**4+1)
for x in range(1,10**2):
    for y in range(1,10**2):
        for z in range(1,10**2):
            n=x**2+y**2+z**2+x*y+y*z+z*x
            if n<=10**4:
                count[n]+=1
for i in range(1,N+1):
    print(count[i])