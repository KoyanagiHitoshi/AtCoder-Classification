A,B,C=map(int,input().split())
print("YES" if any((A*i)%B==C for i in range(1,B+1)) else "NO")