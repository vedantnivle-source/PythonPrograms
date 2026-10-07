def find_missing_number(numbers):
    n = len(numbers) + 1
    total = n * (n + 1) // 2

    return total - sum(numbers)


print(find_missing_number([1, 2, 3, 5]))
