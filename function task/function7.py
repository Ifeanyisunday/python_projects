collections = [7, 19, 7, 40, 19, 6, 25, 46, 33, 40]


def largest(numbers):
    large = 0
    for index in range(0, len(collections)):
        if numbers[index] > large:
            large = numbers[index]
    return large


print(largest(collections))