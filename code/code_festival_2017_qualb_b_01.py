N=int(input())
D=list(map(int,input().split()))
M=int(input())
T=list(map(int,input().split()))
d,t={},{}
for diff in D:
    if diff in d:
        d[diff]+=1
    else:
        d[diff]=1
for diff in T:
    if diff in t:
        t[diff]+=1
    else:
        t[diff]=1
flag=True
for diff in list(set(T)):
    if diff not in d or t[diff]>d[diff]:
        flag=False
print("YES" if flag else "NO")