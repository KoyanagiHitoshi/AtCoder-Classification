A,B=map(int,input().split())
A,B=abs(A),abs(B)
print("Ant" if A<B else "Bug" if A>B else "Draw")