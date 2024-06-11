def print_obj(num):
    output = {}
    count = 0
    for number in num:
        if number == num:
            output[number] = output[count + 1]
    return output


number1 = [2, 5, 3, 3, 2, 3, 5]
print(print_obj(number1))
