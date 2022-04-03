N=int(input())
s=input()
t=input()
overlap=N
for i in range(N):
    if s[i:]==t[:N-i]:
        overlap=i
        break
print(N+overlap)