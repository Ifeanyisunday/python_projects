collections = [7, 19, 7, 40, 19, 6, 25, 46, 33, 40]


def average(numbers):
    total = 0
    for index in range(0, len(collections)):
        total = total + collections[index]
    return total / len(collections)


print(average(collections))
