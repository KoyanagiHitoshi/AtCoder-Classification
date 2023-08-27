N = 11
print("Prime" if all(N % i for i in range(2, int(N**.5)+1)) else "Not prime")
