N,M=map(int,input().split())
s=[list(map(int,input().split()))[1:] for m in range(M)]
p=list(map(int,input().split()))
count=0
for bit in range(1<<N):
    flag=True
    for m in range(M):
        on=0
        for n in range(N):
            if (bit>>n)&1 and n+1 in s[m]:
                on+=1
        if on%2!=p[m]:
            flag=False
    if flag:
        count+=1
print(count)