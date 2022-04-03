N=int(input())
p=sorted(int(input()) for i in range(N))
print(sum(p[:-1])+p[-1]//2)