N=input()
T,A=map(int,input().split())
H=list(map(int,input().split()))
diff=[abs(A-(T-h*0.006)) for h in H]
print(diff.index(min(diff))+1)