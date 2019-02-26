#!/usr/bin/env python
# -*- conding: utf-8 -*-

N = int(input())
S = input()
ans = 0 
for i in range(1, N):
    p = set(S[:i])
    b = set(S[i:])
    ans = max(ans, len(p&b))
print(ans)
