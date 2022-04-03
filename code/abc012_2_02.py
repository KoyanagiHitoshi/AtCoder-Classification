n=int(input())
h=n//3600
m=(n%3600)//60
s=n%60
print("%02d:%02d:%02d"%(h,m,s))