S = 7000
K = 2500
print([1 for y in range(K) for x in range(K) if 0 <= S-x-y <= K].count(1))
