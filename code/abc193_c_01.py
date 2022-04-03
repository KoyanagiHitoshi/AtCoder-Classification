N=int(input())
s=set()
for a in range(2,int(N**.5)+1):
    x=a*a
    while x<=N:
        s.add(x)
        x*=a
print(N-len(s))