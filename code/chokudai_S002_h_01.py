n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    print(abs(a-b) if a-b!=0 else "-1")