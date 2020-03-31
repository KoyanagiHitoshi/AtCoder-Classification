n=int(input())
ab=[list(map(int,input().split())) for i in range(n)]
ab=sorted(ab)[::-1]
print(sum(ab[0]))