for num in range(2, 10):
    i = num
    Factoring = []
    flag = True
    while flag:
        for j in range(2, num+1):
            if i % j == 0:
                i = i/j
                if i == 1:
                    flag = False
                Factoring.append(j)
                break
    if len(Factoring) == 1:
        print(num, "is a prime")
    else:
        print(num, Factoring)
