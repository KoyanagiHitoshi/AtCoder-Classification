#!/usr/bin/env python
# -*- conding: utf-8 -*-

a,b=map(lambda x:(int(x)+13)%15,input().split())
print("Alice" if a>b else "Bob" if a<b else "Draw")
