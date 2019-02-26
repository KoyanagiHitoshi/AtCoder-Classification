#!/usr/bin/env python
# -*- conding: utf-8 -*-

input()
l=map(str,input().split())
print("Three" if len(set(l))==3 else "Four")
