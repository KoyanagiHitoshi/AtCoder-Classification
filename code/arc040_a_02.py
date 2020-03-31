N=int(input())
takahashi=0
aoki=0
for i in range(N):
    s=input()
    takahashi+=s.count("R")
    aoki+=s.count("B")
print("TAKAHASHI" if takahashi>aoki else "AOKI" if takahashi<aoki else "DRAW")