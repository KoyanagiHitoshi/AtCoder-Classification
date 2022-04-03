N=int(input())
A=list(map(int,input().split()))
count=1
sign=0
for i in range(N-1):
    diff=A[i+1]-A[i]
    if sign*diff<0:
        count+=1
        sign=0
    elif sign==0:
        sign=diff
print(count)