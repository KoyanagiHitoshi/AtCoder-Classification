a,b,c,k=map(int,input().split())
s,t=map(int,input().split())
print(a*s+b*t-(s+t)*c*(s+t>=k))