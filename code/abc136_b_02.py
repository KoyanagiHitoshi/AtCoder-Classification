N=int(input())
print(sum(len(str(i))%2==1 for i in range(1,N+1)))