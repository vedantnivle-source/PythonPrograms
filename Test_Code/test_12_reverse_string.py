def reverse_string(text):
    reverse = ""

    for char in text:
        reverse = char + reverse

    return reverse


assert reverse_string("Hello") == "olleH"
assert reverse_string("Python") == "nohtyP"
assert reverse_string("AI") == "IA"

print("All test cases passed!")
