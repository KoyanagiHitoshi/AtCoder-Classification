N=int(input())
d=sorted(map(int,input().split()))
print(d[N//2]-d[N//2-1])