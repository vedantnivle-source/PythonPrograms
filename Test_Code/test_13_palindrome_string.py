def is_palindrome_string(text):
    reverse = ""

    for char in text:
        reverse = char + reverse

    return text == reverse


assert is_palindrome_string("madam") == True
assert is_palindrome_string("hello") == False
assert is_palindrome_string("level") == True
assert is_palindrome_string("python") == False

print("All test cases passed!")
