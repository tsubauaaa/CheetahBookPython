def best_invitation(first, second):
    ans = 0
    for i in range(len(first)):
        f_ans = 0
        s_ans = 0
        for j in range(len(first)):
            if first[i] == first[j] or first[i] == second[j]:
                f_ans += 1
            elif second[i] == second[j] or second[i] == first[j]:
                s_ans += 1
        ans = max(f_ans, s_ans, ans)
    return ans


# print(
#     best_invitation(
#         ["fishing", "gardening", "swimming", "fishing"],
#         ["hunting", "fishing", "fishing", "biting"],
#     )
# )
