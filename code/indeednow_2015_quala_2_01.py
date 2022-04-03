from collections import Counter
N=int(input())
anagram=Counter("indeednow")
for i in range(N):
    S=Counter(input())
    print("YES" if S==anagram else "NO")