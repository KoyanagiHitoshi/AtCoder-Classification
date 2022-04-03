A,B,C=map(int,input().split())
if A==B==C:
    print(0 if A%2 else -1)
else:
    count=0
    while A%2==B%2==C%2==0:
        A,B,C=(B+C)/2,(C+A)/2,(A+B)/2
        count+=1
    print(count)