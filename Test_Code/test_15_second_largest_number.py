def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()

    return unique_numbers[-2]


assert second_largest([10, 20, 5, 30, 15]) == 20
assert second_largest([5, 1, 8, 3]) == 5
assert second_largest([10, 10, 5, 20]) == 10

print("All test cases passed!")
