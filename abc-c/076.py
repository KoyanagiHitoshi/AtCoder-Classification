#!/usr/bin/env python
# -*- conding: utf-8 -*-

import re
s=input().replace("?",".")
t=input()
for i in range(len(s)-len(t)+1):
    if re.match(s[i:i+len(t)],t):
        s=s.replace(".","a")
        print(s[:i]+t+s[i+len(t):])
        exit()
print("UNRESTORABLE")
        
