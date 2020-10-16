def digits(base):
    ans = []
    for n in range(2, base):
        ok = True
        for i in range(base):
            for j in range(base):
                for k in range(base):
                    if (i + j * base + k * base * base) % n == 0 and (
                        i + j + k
                    ) % n != 0:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                break
        if ok:
            ans.append(n)
    return ans


# print(digits(10))
