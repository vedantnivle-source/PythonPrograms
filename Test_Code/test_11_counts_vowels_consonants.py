def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    for char in text.lower():
        if char.isalpha():
            if char in "aeiou":
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants


assert count_vowels_consonants("Hello World") == (3, 7)
assert count_vowels_consonants("Python") == (1, 5)
assert count_vowels_consonants("AI") == (2, 0)

print("All test cases passed!")
