n=int(input())
p=list(map(int,input().split()))
print(len([1 for i in range(n-2) if sorted(p[i:i+3])[1]==p[i+1]]))