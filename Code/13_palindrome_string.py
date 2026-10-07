def is_palindrome_string(text):
    reverse = ""

    for char in text:
        reverse = char + reverse

    return text == reverse


print(is_palindrome_string("madam"))
