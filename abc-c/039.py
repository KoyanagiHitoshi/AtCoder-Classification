#!/usr/bin/env python
# -*- conding: utf-8 -*-

S=input()[0:12]
key="WBWBWWBWBWBW"*2
ans=["Do","","Re","","Mi","Fa","","So","","La","","Si"]
print(ans[(key.find(S))])
