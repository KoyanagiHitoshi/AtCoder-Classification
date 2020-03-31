from collections import Counter
N,K=map(int,input().split())
S=input()
cand=sorted(S)
mismatch=0
ans=''
for i in range(N):
    counter=Counter(S[:i+1])-Counter(list(ans))
    s=sum(counter.values())
    for c in cand[:]:
        miss=mismatch+(c!=S[i])
        diff=s-(counter[c]>0)
        if miss+diff<=K:
            ans+=c
            cand.remove(c)
            mismatch=miss
            break
print(ans)