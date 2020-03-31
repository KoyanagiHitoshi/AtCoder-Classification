s=input()
op=["+","-"]
for i in op:
    for j in op:
        for k in op:
            f=s[0]+i+s[1]+j+s[2]+k+s[3]
            if eval(f)==7:
                print(f+"=7")
                exit()