S=input()
total=0
for i in range(2**(len(S)-1)):
    formula=S[0]
    for j in range(len(S)-1):
        if i&(1<<j):
            formula+="+"
        formula+=S[j+1]
    total+=eval(formula)
print(total)