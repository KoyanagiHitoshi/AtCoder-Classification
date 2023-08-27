S = 7000
K = 2500
print(sum(0 <= S-x-y <= K for y in range(K) for x in range(K)))
