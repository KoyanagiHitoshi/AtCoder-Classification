D,N=map(int,input().split())
numbers=[int(pow(100,D)*i) for i in range(1,N+2)]
print(numbers[N-1] if N!=100 else numbers[N])