S=input()
right=[0]*(len(S)+1)
for i in range(len(S)):
    if S[i]=="<":
        right[i+1]=right[i]+1
left=[0]*(len(S)+1)
for i in range(len(S)-1,-1,-1):
    if S[i]==">":
        left[i]=left[i+1]+1
total=0
for i in range(len(S)+1):
    total+=max(right[i],left[i])
print(total)