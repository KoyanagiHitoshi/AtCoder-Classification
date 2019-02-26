#!/usr/bin/env python
# -*- conding: utf-8 -*-

input()
a=input().split()
input()
a+=input().split()
print("YES" if len(a)==len(set(a)) else "NO")
