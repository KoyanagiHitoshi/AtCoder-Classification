#!/usr/bin/env python
# -*- conding: utf-8 -*-

import functools,fractions
n=input()
a=list(map(int,input().split()))
print(functools.reduce(fractions.gcd,a))
