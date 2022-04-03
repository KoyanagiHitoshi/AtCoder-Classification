N,K=map(int,input().split())
x=sorted(map(int,input().split()))
time=[]
for i in range(N-K+1):
    left=x[i]
    right=x[i+K-1]
    time.append(min(abs(left)+abs(right-left),abs(right)+abs(left-right)))
print(min(time))