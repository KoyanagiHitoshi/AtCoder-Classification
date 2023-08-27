N = 3
for bit in range(1 << N):
    print(bit, end=":{")
    for number in range(N):
        if bit & (1 << number):
            print(number, end=",")
    print("}")
