N=int(input())
S=input()
print(bytes((s-65+N)%26+65 for s in S.encode()).decode())