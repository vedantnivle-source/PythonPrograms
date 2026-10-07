def reverse_number(number):
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10

    return reverse


assert reverse_number(12345) == 54321
assert reverse_number(1237) == 7321
assert reverse_number(10) == 1

print("All test cases passed!")
