def best_invitation(first, second):
    dic = {}
    for i in range(len(first)):
        dic[first[i]] = 0
        dic[second[i]] = 0
    for i in range(len(first)):
        dic[first[i]] += 1
        dic[second[i]] += 1
    ans = 0
    for k in dic:
        if ans < dic[k]:
            ans = dic[k]
    return ans


# print(
#     best_invitation(
#         ["fishing", "gardening", "swimming", "fishing"],
#         ["hunting", "fishing", "fishing", "biting"],
#     )
# )
