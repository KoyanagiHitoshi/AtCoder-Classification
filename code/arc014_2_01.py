N=int(input())
W=[input() for i in range(N)]
said=[]
for i in range(N):
    if i==0:
        said.append(W[0])
    else:
        if W[i] in said or W[i-1][-1]!=W[i][0]:
            print("WIN" if i%2==1 else "LOSE")
            break
        else:
            said.append(W[i])
else:
    print("DRAW")