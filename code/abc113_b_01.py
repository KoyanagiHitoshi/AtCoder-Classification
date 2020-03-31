n=int(input())
t,a=map(int,input().split())
hi=[int(_) for _ in input().split()]
z=[abs(a-(t-x*0.006)) for x in hi]
print(z.index(min(z))+1)