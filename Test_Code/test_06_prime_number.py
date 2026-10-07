def check_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


assert check_prime(7) == True
assert check_prime(10) == False
assert check_prime(2) == True
assert check_prime(1) == False

print("All test cases passed!")
