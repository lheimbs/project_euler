
def is_prime(x):
    if x <= 3:
        return x > 1
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i ** 2 <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True

