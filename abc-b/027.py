#!/usr/bin/env python
# -*- conding: utf-8 -*-

n = int(input())
a = list(map(int, input().split()))
if sum(a) % n != 0:
    print(-1)
else:
    num = 0
    r = sum(a) / n
    for i in range(n):
        if sum(a[:i + 1]) != r * (i + 1):
            num += 1

    print(num)
