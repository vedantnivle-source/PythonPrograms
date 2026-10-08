def find_duplicates(numbers):
    duplicates = []

    for number in numbers:
        if numbers.count(number) > 1 and number not in duplicates:
            duplicates.append(number)

    return duplicates


assert find_duplicates([1,2,3,2,4,3,5,4])==[2,3,4]
assert find_duplicates([3,5,7,2,4,0,3,7,5,4])==[3,5,7,4]
assert find_duplicates([0,6,8,9,6])==[6]
print("All test cases passed!")
