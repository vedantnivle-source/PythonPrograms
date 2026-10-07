def sum_of_digits(number):
    total = 0

    while number > 0:
        digit = number % 10
        total = total + digit
        number = number // 10

    return total


assert sum_of_digits(12345) == 15
assert sum_of_digits(123) == 6
assert sum_of_digits(999) == 27
assert sum_of_digits(10) == 1

print("All test cases passed!")
