def simple_int(n):
    k = 0
    lk = 0

    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                k = k + 1
        if k == 0:
            lk += 1
        else:
            k = 0
    return lk

print(simple_int(100))