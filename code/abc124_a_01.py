a,b=map(int,input().split())
print(2*max(a,b)-1 if abs(a-b)>1 else a+b)