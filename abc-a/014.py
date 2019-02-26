#!/usr/bin/env python
# -*- conding: utf-8 -*-

a=int(input())
b=int(input())
print((((a//b)+1)*b-a) if a%b else "0")
