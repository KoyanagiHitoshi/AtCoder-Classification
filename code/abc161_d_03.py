from collections import deque
K=int(input())
queue=deque(list(range(1,10)))
for i in range(K):
    k=queue.popleft()
    mod=k%10
    for diff in range(mod-1,mod+2):
        if diff<0 or 9<diff:
            continue
        queue.append(10*k+diff)
print(k)