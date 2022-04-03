N=sorted(input())[::-1]
ans=0
for bit in range(1<<len(N)):
    left,right=[],[]
    for i in range(len(N)):
        if (bit>>i)&1:
            left.append(N[i])
        else:
            right.append(N[i])
    if len(left)==0 or len(right)==0:
        continue
    ans=max(ans,int("".join(left))*int("".join(right)))
print(ans)