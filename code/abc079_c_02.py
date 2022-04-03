ABCD=input()
digits=3
ops=[""]*(digits+1)
for i in range(1<<digits):
    for j in range(digits):
        if (i>>j)&1:
            ops[j]="+"
        else:
            ops[j]="-"
    evals=""
    for num,op in zip(ABCD,ops):
        evals+=num+op
    if eval(evals)==7:
        print(evals+"=7")
        break