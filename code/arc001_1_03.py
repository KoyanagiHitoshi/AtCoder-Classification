N=input()
C=input()
counter=[C.count(c) for c in "1234"]
print(max(counter),min(counter))