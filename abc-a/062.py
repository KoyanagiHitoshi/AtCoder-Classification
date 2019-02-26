#!/usr/bin/env python
# -*- conding: utf-8 -*-

x,y=input().split()
a={"1","3","5","7","8","10","12"}
b={"4","6","9","11"}
print("Yes" if {x,y}<=a or {x,y}<=b else "No")
