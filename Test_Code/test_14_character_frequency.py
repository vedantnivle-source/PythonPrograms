ef character_frequency(text):
    frequency = {}

    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency


assert character_frequency("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
assert character_frequency("aaa") == {'a': 3}
assert character_frequency("python") == {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}

print("All test cases passed!")
