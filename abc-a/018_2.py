#!/usr/bin/env python
# -*- conding: utf-8 -*-

X=[int(input()) for i in range(3)]
for x in X:print(3-sorted(X).index(x))
