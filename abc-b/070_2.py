#!/usr/bin/env python
# -*- conding: utf-8 -*-

a,b,c,d=map(int,input().split())
print(max(min(d,b)-max(c,a),0))
