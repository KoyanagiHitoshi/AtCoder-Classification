#!/usr/bin/env python
# -*- conding: utf-8 -*-

input()
print(sum(sorted(map(int,input().split()))[::-1][::2]))

