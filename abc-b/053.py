#!/usr/bin/env python
# -*- conding: utf-8 -*-

s=input()
print(len(s)-s[::-1].index("Z")-s.index("A"))
