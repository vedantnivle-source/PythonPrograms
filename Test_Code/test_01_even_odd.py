def check_even_odd(number):
    if number % 2==0:
        return"even"
    else:
        return"odd"
    assert check_even_odd(10)=="even"
    assert check_even_odd(5)=="odd"
    print("All the cases passed")
