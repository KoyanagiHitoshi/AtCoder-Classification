from collections import deque
S=deque(input())
Q=int(input())
reverse=0
for q in range(Q):
    Query=list(input().split())
    T=Query[0]
    if T=="1":
        reverse+=1
    if T=="2":
        F,C=Query[1],Query[2]
        if F=="1" and reverse%2==0 or F=="2" and reverse%2==1:
            S.appendleft(C)
        else:
            S.append(C)
S="".join(S)
print(S if reverse%2==0 else S[::-1])