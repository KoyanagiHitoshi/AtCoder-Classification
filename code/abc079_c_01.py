A,B,C,D=input()
digits=3
op=[""]*digits
for i in range(1<<digits):
    for j in range(digits):
        if (i>>j)&1:
            op[j]="+"
        else:
            op[j]="-"
    if eval(A+op[0]+B+op[1]+C+op[2]+D)==7:
        print(A+op[0]+B+op[1]+C+op[2]+D+"=7")
        break