import itertools
S=input()
s=[int(w) for w in S]
ans=len(S)
for bits in itertools.product((True,False),repeat=len(S)):
    digit_sum=0
    digit_del=0
    for i,bit in enumerate(bits):
        if bit:
            digit_sum+=s[i]
        else:
            digit_del+=1
    if digit_sum%3==0:
        ans=min(ans,digit_del)
print(-1 if ans==len(S) else ans)