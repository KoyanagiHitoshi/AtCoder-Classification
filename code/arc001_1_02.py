input()
C=input()
print(*sorted(C.count(c) for c in "1234")[::-3])