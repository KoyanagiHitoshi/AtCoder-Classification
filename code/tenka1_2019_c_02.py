input()
S=input()
dot=S.count(".")
ans=dot
sharp=0
for s in S:
    if s=="#":sharp+=1
    else:dot-=1
    ans=min(ans,sharp+dot)
print(ans)