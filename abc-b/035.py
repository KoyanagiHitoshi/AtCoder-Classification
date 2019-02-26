#!/usr/bin/env python
# -*- conding: utf-8 -*-

s=input()
d=abs(s.count("L")-s.count("R"))+abs(s.count("U")-s.count("D"))
q=s.count("?")
if int(input())==1:print(d+q)
else:print(max(len(s)%2,d-q))

