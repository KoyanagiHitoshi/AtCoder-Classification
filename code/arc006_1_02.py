E=[int(i) for i in input().split()]
B=int(input())
L=[int(i) for i in input().split()]
match=6-len(set(E)-set(L))
if match==5 and B in L:
    print(2)
else:
    print({6:1,5:3,4:4,3:5}.get(match,0))