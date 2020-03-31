n,t=map(int,input().split())
a=b=0
for i in range(n):
    s=int(input())
    if s>b:a+=s-b
    b=s+t
print(b-a)