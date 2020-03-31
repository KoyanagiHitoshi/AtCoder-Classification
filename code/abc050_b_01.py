n=int(input())
t=[int(_) for _ in input().split()]
m=int(input())
p=[[int(j) for j in input().split()] for i in range(m)]
for i in range(m):print(sum(t)-t[p[i][0]-1]+p[i][1])