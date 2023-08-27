def divisors(num: int) -> list:
    ascend, descend = [], []
    i = 1
    while i*i <= num:
        if num % i == 0:
            ascend.append(i)
            if i != num//i:
                descend.append(num//i)
        i += 1
    return ascend + descend[::-1]


N = 100
print(divisors(N))
