N=int(input())
SP=[]
for i in range(N):
    S,P=input().split()
    SP.append([S,int(P),i+1])
SP.sort(key=lambda sp:(sp[0],-sp[1]))
for sp in SP:
    print(sp[2])