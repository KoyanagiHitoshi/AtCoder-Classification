A,B=map(int,input().split())
E=[]
adjust=0
if A==B:
    for i in range(1,A+1):
        E.append(i)
        E.append(-i)
elif A>B:
    for i in range(1,A+1):
        E.append(i)
    for i in range(1,B):
        E.append(-i)
    for i in range(B,A+1):
        adjust+=i
    E.append(-adjust)
else:
    for i in range(1,B+1):
        E.append(-i)
    for i in range(1,A):
        E.append(i)
    for i in range(A,B+1):
        adjust+=i
    E.append(adjust)
print(*E)