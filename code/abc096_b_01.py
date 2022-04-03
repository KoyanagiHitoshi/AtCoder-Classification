ABC=list(map(int,input().split()))
K=int(input())
for k in range(K):
    maximum=max(ABC)
    ABC.remove(maximum)
    ABC.append(maximum*2)
print(sum(ABC))