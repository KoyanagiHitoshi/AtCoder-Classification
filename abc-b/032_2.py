#!/usr/bin/env python
# -*- conding: utf-8 -*-

s=input()
k=int(input())
print(len(set(s[i:i+k] for i in range(len(s)-k+1))))


