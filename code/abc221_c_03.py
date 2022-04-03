N=sorted(input())[::-1]
ans=0
for bit in range(1<<len(N)):
    left,right=0,0
    for i in range(len(N)):
        if (bit>>i)&1:
            left=left*10+int(N[i])
        else:
            right=right*10+int(N[i])
    if left==0 or right==0:
        continue
    ans=max(ans,left*right)
print(ans)