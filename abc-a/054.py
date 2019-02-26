#!/usr/bin/env python
# -*- conding: utf-8 -*-

a,b=map(int,input().split())
if a==1:a+=13
if b==1:b+=13
print("Alice" if a>b else "Draw" if a==b else "Bob")
