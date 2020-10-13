def encrypt(numbers):
    seki = 1
    for i in range(len(numbers)):
        seki *= numbers[i]

    ans = 0

    for i in range(len(numbers)):
        ans = max(ans, seki / numbers[i] * (numbers[i] + 1))

    return int(ans)


# print(encrypt([1, 2, 3]))
