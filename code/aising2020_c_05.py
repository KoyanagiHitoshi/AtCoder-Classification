from itertools import product
N=int(input())
f=[0]*N
for x,y,z in product(range(1,100),repeat=3):
    n=x**2+y**2+z**2+x*y+y*z+z*x
    if n<=N:
        f[n-1]+=1
print(*f,sep="\n")