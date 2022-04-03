N=int(input())
S=input()
count=0
same=0
for i in range(N-1):
    if S[i]==S[i+1]:
        same+=1
    else:
        same=0
    count+=same
print(count)