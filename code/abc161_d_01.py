from collections import deque
K=int(input())
queue=deque([1,2,3,4,5,6,7,8,9])
for i in range(K):
    k=queue.popleft()
    if k%10!=0:
        queue.append(10*k+(k%10)-1)
    queue.append(10*k+(k%10))
    if k%10!=9:
        queue.append(10*k+(k%10)+1)
print(k)