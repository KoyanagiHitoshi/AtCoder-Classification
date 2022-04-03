N=int(input())
S=list(map(int,input().split()))
s=[]
for a in range(1,334):
    for b in range(1,334):
        if 4*a*b+3*a+3*b<=1000:
            s.append(4*a*b+3*a+3*b)
X=set(S)-set(s)
count=0
for x in X:
    count+=S.count(x)
print(count)