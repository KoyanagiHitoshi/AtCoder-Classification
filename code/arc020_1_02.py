A,B=map(abs,map(int,input().split()))
print("Ant" if A<B else "Bug" if A>B else "Draw")