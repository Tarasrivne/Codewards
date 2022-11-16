def all_numb(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]
sum_numb = all_numb([1,2,3,4,5,6,9])
print(sum_numb)