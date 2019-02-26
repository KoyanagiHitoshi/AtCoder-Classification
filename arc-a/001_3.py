#!/usr/bin/env python
# -*- conding: utf-8 -*-

input()
C=input()
print(*sorted(C.count(c) for c in "1234")[::-3])
