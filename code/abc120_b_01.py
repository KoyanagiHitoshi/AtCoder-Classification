A,B,K=map(int,input().split())
a=[]
for i in range(1,A+1):
    if A%i==0:a.append(i)
b=[]
for i in range(1,B+1):
    if B%i==0:b.append(i)
c=set()
c=sorted(list(set(a)&set(b)))[::-1]
print(c[K-1])