l=[int(input()) for i in range(5)]
ans=0
m=10
for i in l:
    mod=i%10
    if mod!=0:
        m=min(m,mod)
        ans+=i+(10-mod)
    else:
        ans+=i
print(ans-(10-m))