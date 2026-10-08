def remove_duplicates(numbers):
    unique_numbers = []

    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    return unique_numbers


assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
assert remove_duplicates([1, 1, 1, 2, 2]) == [1, 2]
assert remove_duplicates([5, 4, 5, 3, 4]) == [5, 4, 3]

print("All test cases passed!")
