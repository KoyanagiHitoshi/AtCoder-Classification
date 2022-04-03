n=int(input())
p=list(map(int,input().split()))
print(sum(p[i+1]==sorted(p[i:i+3])[1] for i in range(n-2)))