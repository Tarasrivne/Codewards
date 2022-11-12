def remove_smallest(numbers):
    if not numbers:
        return numbers

    lowest_num = numbers[0]

    for num in numbers:
        if num < lowest_num:
            lowest_num = num
    index = 0
    for num in numbers:

        if num == lowest_num:
            break
        index += 1
    numbers_copy = numbers.copy()
    del numbers_copy[index]
    print(lowest_num)
    return numbers_copy

a = remove_smallest([2,3,4,1,5,6])
print(a)
