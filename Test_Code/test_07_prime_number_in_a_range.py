def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def prime_numbers_in_range(start, end):
    primes = []

    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)

    return primes


assert prime_numbers_in_range(1, 10) == [2, 3, 5, 7]
assert prime_numbers_in_range(10, 20) == [11, 13, 17, 19]

print("All test cases passed!")
