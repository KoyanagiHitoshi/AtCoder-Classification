#!/usr/bin/env python
# -*- conding: utf-8 -*-

s=reversed([input() for i in range(int(input()))])
for x in zip(*s):print("".join(x))
