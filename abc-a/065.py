#!/usr/bin/env python
# -*- conding: utf-8 -*-

x,a,b=map(int,input().split())
print('dangerous'if x<b-a else'safe' if a<b else'delicious')
