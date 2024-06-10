collections = [7, 19, 7, 40, 19, 6, 25, 46, 33, 40]


def sum_of_odd_index(numbers):
    total = 0
    for index in range(0, len(collections)):
        if index % 2 != 0:
            total = total + collections[index]
    return total


print(sum_of_odd_index(collections))