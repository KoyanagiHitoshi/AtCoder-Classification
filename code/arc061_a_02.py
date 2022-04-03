S=input()
total=0
for i in range(len(S)):
    for j in range(i+1):
        total+=int(S[-(i+1)])*(10**j)*(2**(len(S)-1))//(2**min(i,j+1))
print(total)