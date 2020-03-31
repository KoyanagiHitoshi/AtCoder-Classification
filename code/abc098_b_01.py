n=int(input())
s=input()
c=0
for i in range(1,n):
    p=set(s[:i])
    b=set(s[i:])
    c=max(c,len(p&b))
print(c)