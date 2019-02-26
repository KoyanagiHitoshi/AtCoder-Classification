#!/usr/bin/env python
# -*- conding: utf-8 -*-

S="XACABABAABABA"
x,y=map(int,input().split())
print("Yes" if S[x]==S[y] else "No")
