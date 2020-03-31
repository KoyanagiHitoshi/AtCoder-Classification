n=int(input())
p=sorted([int(input()) for i in range(n)])
print(p[-1]//2+sum(p[:-1]))