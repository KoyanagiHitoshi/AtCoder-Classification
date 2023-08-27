import re
x = ["A", "C", "AC", "CA", "ACA", "CAC", "ac", "xAxCx", "xACx"]
for s in x:
    print(re.split("[^AC]", s))
