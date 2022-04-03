N=int(input())
s,t=[0]*N,[0]*N
for i in range(N):
    s[i],t[i]=input().split()
X=input()
print(sum(list(map(int,t[s.index(X)+1:]))))