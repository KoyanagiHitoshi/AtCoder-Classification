#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,k=map(int,input().split())
print(sum(sorted(map(int,input().split()))[-k:]))

