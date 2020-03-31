n,m,x=map(int,input().split())
s=sum(int(_)<x for _ in input().split())
print(min(s,m-s))