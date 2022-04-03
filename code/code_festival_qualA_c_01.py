A,B=map(int,input().split())
A-=1
print(B//4-B//100+B//400-(A//4-A//100+A//400))