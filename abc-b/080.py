#!/usr/bin/env python
# -*- conding: utf-8 -*-

n=input()
print("No" if int(n)%sum(map(int,n)) else "Yes")
