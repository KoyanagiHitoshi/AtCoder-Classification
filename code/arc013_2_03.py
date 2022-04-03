C=int(input())
NML=[sorted(map(int,input().split())) for i in range(C)]
n,m,l=map(max,zip(*NML))
print(n*m*l)