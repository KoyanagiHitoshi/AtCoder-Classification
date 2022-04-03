import collections
N=int(input())
A=list(map(int,input().split()))
Q=collections.deque(A)
while len(Q)>2:
    x=Q.popleft()
    y=Q.popleft()
    Q.append(max(x,y))
print(A.index(min(Q))+1)