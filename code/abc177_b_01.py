S=input()
T=input()
diff=len(T)
for i in range(len(S)-len(T)+1):
    count=0
    for j in range(len(T)):
        if S[i+j]!=T[j]:
            count+=1
    diff=min(diff,count)
print(diff)