def compareTriplets(a, b):
    sum_points_a = 0
    sum_points_b = 0
    for i, j in zip(a, b):
        if i > j:
            sum_points_a += 1
        elif i == j:
            pass
        else:
            sum_points_b += 1
    return sum_points_a, sum_points_b

print(compareTriplets([17, 28, 30,],[99, 16, 8]))



