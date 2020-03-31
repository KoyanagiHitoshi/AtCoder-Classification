input()
A=map(int,input().split())
print(1/sum(1/a for a in A))