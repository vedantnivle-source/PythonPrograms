def find_missing_number(numbers):
    n = len(numbers) + 1
    total = n * (n + 1) // 2

    return total - sum(numbers)


assert find_missing_number([1, 2, 3, 5]) == 4
assert find_missing_number([1, 2, 4, 5]) == 3
assert find_missing_number([1, 3, 4, 5]) == 2

print("All test cases passed!")
