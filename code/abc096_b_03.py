ABC=[int(i) for i in input().split()]
K=int(input())
print(sum(ABC)-max(ABC)+max(ABC)*2**K)