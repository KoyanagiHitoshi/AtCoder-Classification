S=input()
total=0
for bit in range(1<<len(S)-1):
    formula=S[0]
    for n in range(len(S)-1):
        if bit&(1<<n):
            formula+="+"
        formula+=S[n+1]
    total+=eval(formula)
print(total)