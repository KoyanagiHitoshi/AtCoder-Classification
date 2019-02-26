#!/usr/bin/env python
# -*- conding: utf-8 -*-

print("Yes" if [4*x+7*y for y in range(101) for x in range(101)].count(int(input())) else "No")
