n,m,x=map(int,input().split())
s=sum(int(i)<x for i in input().split())
print(min(s,m-s))