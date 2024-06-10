collections = [7, 19, 7, 40, 19, 6, 25, 46, 33, 40]


def smallest(numbers):
    small = numbers[0]
    for index in range(0, len(numbers)):
        if numbers[index] < small:
            small = numbers[index]
    return small


print(smallest(collections))