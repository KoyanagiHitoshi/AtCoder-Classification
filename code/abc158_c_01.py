A,B=map(int,input().split())
for money in range(1,1001):
    if int(money*0.08)==A and int(money*0.1)==B:
        print(money)
        break
else:
    print(-1)