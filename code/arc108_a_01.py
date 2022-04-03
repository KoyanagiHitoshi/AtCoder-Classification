S,P=map(int,input().split())
for M in range(10**6+1):
    if M*(S-M)==P:
        print("Yes")
        break
else:
    print("No")