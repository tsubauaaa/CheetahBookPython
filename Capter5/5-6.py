def digits(base):
    ans = []
    for n in range(2, base):
        if (base - 1) % n == 0:
            ans.append(n)
    return ans


print(digits(10))
