#!/usr/bin/env python
# -*- conding: utf-8 -*-

a,b=map(int,input().split())
print("Draw" if a==b else "Bob" if (a+13)%15<(b+13)%15 else "Alice")
