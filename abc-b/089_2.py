#!/usr/bin/env python
# -*- conding: utf-8 -*-

input()
print("Three" if len(set(map(str,input().split())))==3 else "Four")
