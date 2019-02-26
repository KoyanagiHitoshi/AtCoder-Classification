#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,m=map(int,input().split())
cnt=[0 for i in range(n+1)]
a=[]
for i in range(m):
    p,y=map(int,input().split())
    a.append((y,p,i))
a.sort()
print(a)
b=[]
for y,p,i in a:
    cnt[p]+=1
    b.append((i,"{0:06}{0:06}".format(p,cnt[p])))
b.sort()
print(b)
for i,r in b:
    print(r)
