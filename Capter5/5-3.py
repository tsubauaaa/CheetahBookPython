def encrypt(numbers):
    ans = 0
    for i in range(len(numbers)):
        seki = 1
        for j in range(len(numbers)):
            if i == j:
                seki *= numbers[j] + 1
            else:
                seki *= numbers[j]
        ans = max(seki, ans)
    return ans


# print(encrypt([1, 2, 3]))
