S,P=map(int,input().split())
for M in range(1,int(P**.5)+1):
    if M*(S-M)==P:
        print("Yes")
        break
else:
    print("No")