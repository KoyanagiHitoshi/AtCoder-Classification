#!/usr/bin/env python
# -*- conding: utf-8 -*-

a,b,c,d=map(int,input().split())
print(['Balanced','Left','Right'][(a+b>c+d)-(a+b<c+d)])
