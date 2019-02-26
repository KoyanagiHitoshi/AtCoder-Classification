#!/usr/bin/env python
# -*- conding: utf-8 -*-

N, T = map(int, input().split())

M = 1001
for i in range(N):
    ci, ti = map(int, input().split())
    if ti <= T:
        M = min(M, ci)
print("TLE" if M==1001 else M)
