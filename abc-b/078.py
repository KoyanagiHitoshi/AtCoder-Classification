#!/usr/bin/env python
# -*- conding: utf-8 -*-

x,y,z=map(int,input().split())
print(x//(y+z)-1 if x%(y+z)<z else x//(y+z))
