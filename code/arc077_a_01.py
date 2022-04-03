from collections import deque
n=int(input())
a=list(map(int,input().split()))
b=deque()
for i in range(n):
    if i%2==0:
        b.append(a[i])
    else:
        b.appendleft(a[i])
if n%2==0:
    print(*b)
else:
    print(*deque(reversed(b)))