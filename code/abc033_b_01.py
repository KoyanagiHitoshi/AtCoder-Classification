n=int(input())
a=[]
l=[]
for i in range(n):
    s,p=input().split()
    a.append(s)
    l.append(int(p))
for i in range(n):
    if l[i]>sum(l)/2:
        print(a[i])
        exit()
print("atcoder")