def the_pouring(capacities, bottles, from_id, to_id):
    for f, t in zip(from_id, to_id):
        sum = bottles[f] + bottles[t]
        bottles[t] = min(sum, capacities[t])
        bottles[f] = sum - bottles[t]
    return bottles


# print(the_pouring([20, 20], [5, 8], [0], [1]))
# print(the_pouring([30, 20, 10], [10, 5, 5], [0, 1, 2], [1, 2, 0]))
# print(
#     the_pouring(
#         [14, 35, 86, 58, 25, 62],
#         [6, 34, 27, 38, 9, 60],
#         [1, 2, 4, 5, 3, 3, 1, 0],
#         [0, 1, 2, 4, 2, 5, 3, 1],
#     )
# )
