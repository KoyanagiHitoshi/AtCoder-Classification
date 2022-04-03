N = int(input())
ST = [input().split() for i in range(N)]
print(sorted(ST, key=lambda x: int(x[1]))[-2][0])