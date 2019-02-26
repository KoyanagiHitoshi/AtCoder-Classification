#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,m,l=map(int,input().split())
p,q,r=map(int,input().split())
v=0
v=max(v,(n//p)*(m//q)*(l//r))
v=max(v,(n//p)*(m//r)*(l//q))
v=max(v,(n//q)*(m//p)*(l//r))
v=max(v,(n//q)*(m//r)*(l//p))
v=max(v,(n//r)*(m//p)*(l//q))
v=max(v,(n//r)*(m//q)*(l//p))
print(v)
