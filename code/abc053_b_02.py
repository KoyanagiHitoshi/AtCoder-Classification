s=input()
print((len(s)-s[::-1].find("Z"))-s.find("A"))