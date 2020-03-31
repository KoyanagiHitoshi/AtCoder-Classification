N=int(input())
S=[list(input()) for i in range(N)]
takahashi=0
aoki=0
for s in S:
    takahashi+=s.count("R")
    aoki+=s.count("B")
print("TAKAHASHI" if takahashi>aoki else "AOKI" if takahashi<aoki else "DRAW")