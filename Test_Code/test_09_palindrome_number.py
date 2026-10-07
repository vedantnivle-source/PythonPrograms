def is_palindrome(number):
    original = number
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10

    return original == reverse


assert is_palindrome(121) == True
assert is_palindrome(123) == False
assert is_palindrome(11) == True
assert is_palindrome(10) == False

print("All test cases passed!")
