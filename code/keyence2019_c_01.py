N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

C=[a-b for a,b in zip(A,B)]

plus=[i for i in C if i>=0]
minus=[i for i in C if i<0]
plus.sort(reverse=True)

sum_minus=sum(minus)
ans=len(minus)

for i in plus:
    if sum_minus>=0:
        break
    sum_minus+=i
    ans+=1

if sum_minus<0:
    ans=-1

print(ans)