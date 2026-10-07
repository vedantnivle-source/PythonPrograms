def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()

    return unique_numbers[-2]


print(second_largest([10, 35, 5, 30, 15]))
