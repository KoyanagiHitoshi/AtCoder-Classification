#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,k=map(int,input().split())
print(sum(sorted([int(_) for _ in input().split()])[-k:]))

