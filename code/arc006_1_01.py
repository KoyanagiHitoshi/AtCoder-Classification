E=set(input().split())
B=input()
L=set(input().split())
match=len(E&L)
ans=0
if match==5 and B in L:
    ans=2
elif match==6:
    ans=1
elif match>2:
    ans=8-match
else:
    ans=0
print(ans)