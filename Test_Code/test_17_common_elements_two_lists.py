def common_elements(list1, list2):
    common = []

    for number in list1:
        if number in list2 and number not in common:
            common.append(number)

    return common


assert common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
assert common_elements([1, 2, 3], [4, 5, 6]) == []
assert common_elements([1, 2, 2, 3], [2, 3, 4]) == [2, 3]

print("All test cases passed!")
