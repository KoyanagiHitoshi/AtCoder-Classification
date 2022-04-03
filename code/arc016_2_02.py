N=int(input())
before="."*9
count=0
for i in range(N):
    x=input()
    for j in range(9):
        if x[j]=="x" or (x[j]=="o" and before[j]!="o"):
            count+=1
    before=x
print(count)