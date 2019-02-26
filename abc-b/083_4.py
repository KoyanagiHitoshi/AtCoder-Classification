#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,a,b=map(int,input().split())
print(sum(i for i in range(n+1) if(a<=sum(map(int,str(i)))<=b)))
