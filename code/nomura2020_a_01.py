H1,M1,H2,M2,K=map(int,input().split())
if M1>M2:
    print(max((H2-H1-1)*60+(60-(M1-M2))-K,0))
else:
    print(max((H2-H1)*60+(M2-M1)-K,0))