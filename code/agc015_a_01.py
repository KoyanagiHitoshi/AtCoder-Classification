N,A,B=map(int,input().split())
if N<2 and A!=B or B<A:print(0)
else:print((A+B*(N-1))-(A*(N-1)+B)+1)