N = 3
for bit in range(1 << N):
    bit_string = [0]*N
    for digit in range(N):
        if (bit >> digit) & 1:
            bit_string[digit] = 1
        else:
            bit_string[digit] = 0
    print(bit_string)
