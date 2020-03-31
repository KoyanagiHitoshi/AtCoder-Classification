N=int(input())
S=[list(input()) for i in range(N)]
diff=sum(s.count("R") for s in S)-sum(s.count("B") for s in S)
print("TAKAHASHI" if diff>0 else "AOKI" if diff<0 else "DRAW")