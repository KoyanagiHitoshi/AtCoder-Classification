input()
S=input()
dot=S.count(".")
ans=dot
count=0
for s in S:
    if s=="#":count+=1
    else:dot-=1
    ans=(min(ans,count+dot))
print(ans)