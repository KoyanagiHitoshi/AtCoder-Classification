K=int(input())
A,B=map(int,input().split())
print("OK" if B//K*K>=A else "NG")