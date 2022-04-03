S,T=input().split()
A,B=map(int,input().split())
U=input()
ball={S:A,T:B}
ball[U]-=1
print(ball[S],ball[T])