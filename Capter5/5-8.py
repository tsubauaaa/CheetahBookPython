def highest_score(friends):
    ans = 0
    n = len(friends[0])
    for i1 in range(n):
        cnt = 0

        for i2 in range(n):
            if i1 == i2:
                continue
            if friends[i1][i2] == "Y":
                cnt += 1
            else:
                for i3 in range(n):
                    if friends[i2][i3] == "Y" and friends[i1][i3] == "Y":
                        cnt += 1
                        break

        ans = max(ans, cnt)

    return ans


print(highest_score(["NYNNN", "YNYNN", "NYNYN", "NNYNY", "NNNYN"]))
