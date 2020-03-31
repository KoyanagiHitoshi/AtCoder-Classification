input()
M=map(int,input().split())
print(sum(80-m for m in M if m<80))