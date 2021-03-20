
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

def is_prime_faster(n):
    if n == 1:
        return False
    if n < 4:
        return True
    if n%2 == 0:
        return False
    if n < 9:
        return True
    r = floor(n**(1/2))
    f = 5
    while f <= r:
        if n%f == 0:
            return False
        if n%(f+2) == 0:
            return False
        f += 6
    return True
