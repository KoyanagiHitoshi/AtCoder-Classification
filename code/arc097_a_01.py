S=input()
K=int(input())
print(sorted(set(S[j:j+i+1] for j in range(len(S)) for i in range(K)))[K-1])