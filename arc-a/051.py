#!/usr/bin/env python
# -*- conding: utf-8 -*-

x,y,r=map(int,input().split())
a,b,c,d=map(int,input().split())
if a<=x-r and x+r<=c and b<=y-r and y+r<=d:print("NO")
else:print("YES")
if max((a-x)**2,(c-x)**2)+max((b-y)**2,(d-y)**2)<=r**2:print("NO")
else:print("YES")
