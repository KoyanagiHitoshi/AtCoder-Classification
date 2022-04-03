N=int(input())
A=max(map(int,input().split()))
B=min(map(int,input().split()))
print(max(0,B-A+1))