N=int(input())
ab=input().split()
K=int(input())
P=input().split()
path=ab+P
print("YES" if len(path)==len(set(path)) else "NO")