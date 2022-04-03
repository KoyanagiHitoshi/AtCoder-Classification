N=int(input())
f=[0]*N
for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            n=x**2+y**2+z**2+x*y+y*z+z*x
            if n<=N:
                f[n-1]+=1
print(*f,sep="\n")