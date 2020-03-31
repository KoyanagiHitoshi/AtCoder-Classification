k,a,b=map(int,input().split())
t=k-(a-1)
print(max(k+1,(t//2)*(b-a)+t%2+a))