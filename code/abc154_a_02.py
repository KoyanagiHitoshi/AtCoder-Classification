S,T=input().split()
A,B=map(int,input().split())
U=input()
ST={S:A,T:B}
ST[U]-=1
print(ST[S],ST[T])