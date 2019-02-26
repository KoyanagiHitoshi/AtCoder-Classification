#!/usr/bin/env python
# -*- conding: utf-8 -*-

s=input()
print("no" if len(s)-len(set(s)) else "yes")
