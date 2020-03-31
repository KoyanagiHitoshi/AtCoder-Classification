l,h=map(int,input().split())
n=int(input())
for i in range(n):
    a=int(input())
    print(l-a if l>a else "0" if h>=a else "-1")