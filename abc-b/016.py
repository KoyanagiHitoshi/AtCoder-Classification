#!/usr/bin/env python
# -*- conding: utf-8 -*-

a,b,c=map(int,input().split())
print("?" if a+b==c and a-b==c else "+" if a+b==c else "-" if a-b==c else "!")
