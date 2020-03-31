n=int(input())
t,a=map(int,input().split())
h=list(map(int,input().split()))
z=[abs(t-x*0.006-a) for x in h]
print(z.index(min(z))+1)