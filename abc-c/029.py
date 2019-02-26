#!/usr/bin/env python
# -*- conding: utf-8 -*-

from itertools import product
[print("".join(i)) for i in product("abc",repeat=int(input()))]
