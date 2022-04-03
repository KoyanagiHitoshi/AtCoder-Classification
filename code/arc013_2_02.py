C=int(input())
NML=[sorted(map(int,input().split())) for i in range(C)]
n,m,l=zip(*NML)
print(max(n)*max(m)*max(l))