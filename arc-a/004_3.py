#!/usr/bin/env python
# -*- conding: utf-8 -*-

import math
p=[list(map(int,input().split())) for i in range(int(input()))]
print(max(math.hypot(a[0]-b[0],a[1]-b[1]) for b in p for a in p))
