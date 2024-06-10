collections = [7, 19, 7, 40, 19, 6, 25, 46, 33, 40]


def find_length_without_len_function(numbers):
    counter = 0
    for number in numbers:
        counter += 1
    return counter


print(find_length_without_len_function(collections))
