N=int(input())
s,t=zip(*[input().split() for i in range(N)])
X=input()
print(sum(map(int,t[s.index(X)+1:])))