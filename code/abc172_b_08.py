S=input()
T=input()
count=0
for i in range(len(S)):
    count+=S[i]!=T[i]
print(count)