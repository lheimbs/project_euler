import utils

primes = []

def is_twice_square(n):
    x = (n/2)**(0.5)
    if x.is_integer():
        return True
    return False

def is_conjecture(n):
    for prime in primes:
        if is_twice_square(n - prime):
            return True
    return False

i = 2
while i:
    if utils.is_prime_faster(i):
        primes.append(i)
        i += 1
        continue
    if not utils.is_even(i):
        if not is_conjecture(i):
            print(i)
            break
    i += 1

