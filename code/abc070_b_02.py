A,B,C,D=map(int,input().split())
time=len(set(map(int,range(A,B+1)))&set(map(int,range(C,D+1))))-1
print(0 if time==-1 else time)