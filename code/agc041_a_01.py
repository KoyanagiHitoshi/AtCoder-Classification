N,A,B=map(int,input().split())
if (B-A)%2:
    print(min(A-1,N-B)+1+(B-A-1)//2)
else:
    print((B-A)//2)