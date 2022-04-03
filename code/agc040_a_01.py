S=input()
a=[0]*(len(S)+1)
for i in range(len(S)):
    if S[i]=="<":
        a[i+1]=max(a[i+1],a[i]+1)
for i in range(len(S)-1,-1,-1):
    if S[i]==">":
        a[i]=max(a[i],a[i+1]+1)
print(sum(a))