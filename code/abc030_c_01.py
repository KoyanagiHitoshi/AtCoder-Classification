import bisect
N,M=map(int,input().split())
X,Y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
count=0
time=0
while time<=a[-1]:
    time=a[bisect.bisect_left(a,time)]+X
    if time<=b[-1]:
        time=b[bisect.bisect_left(b,time)]+Y
        count+=1
    else:
        break
print(count)