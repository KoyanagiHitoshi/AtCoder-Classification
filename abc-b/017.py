#!/usr/bin/env python
# -*- conding: utf-8 -*-

import re
print("NO" if re.sub(r"ch|o|k|u","",input()) else "YES")
