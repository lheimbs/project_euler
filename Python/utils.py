import sys
from math import floor
from itertools import chain
import numpy as np


def is_even(n):
    return n % 2 == 0


def get_N():
    if len(sys.argv) > 1 and sys.argv[1].isnumeric():
        return int(sys.argv[1])
    return None


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
    if n%3 == 0:
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


def get_prime_factors(n):
    factors = []
    if n%2 == 0:
        n = n // 2
        last_factor = 2
        factors.append(2)
        while n%2 == 0:
            n = n // 2
    else:
        last_factor = 1

    factor = 3
    while n > 1:
        if n%factor == 0:
            n = n // factor
            last_factor = factor
            factors.append(factor)
            while n%factor == 0:
                n = n // factor
        factor += 2
    return factors


def get_prime_factors_faster(n):
    l = []
    for i in chain([2], range(3, n//2 + 1)):
        while n % i == 0:
            l.append(i)
            n = n // i
        if i > n:
            break
    return l


def quadratic_sieve(n):
    # taken from https://projecteuler.net/overview=010
    limit = int(n)
    crosslimit = int(limit ** (1/2))
    sieve = np.zeros(limit, dtype=bool)
    for n in range(4, limit, 2):
        sieve[n] = True
    for n in range(3, crosslimit, 2):
        if not sieve[n]:
            for m in range(n*n, limit, 2*n):
                sieve[m] = True
    sum = 0
    for n in range(2, limit):
        if not sieve[n]:
            sum += n
    return sum


def sieve_optm(n):
    limit = int(n)
    sievebound = (limit-1) // 2
    sieve = np.zeros(sievebound, dtype=bool)
    crosslimit = (int(limit ** (1/2))-1) // 2
    print(sievebound, len(sieve), crosslimit)
    i = 1
    while i < crosslimit:
        if not sieve[i]:
            j = 2 * i * (i+1)
            while j < sievebound:
                sieve[j] = True
                j = j + (2*i+1)
        i += 1
    sum = 2
    i = 1
    print(f"zeros: {len(sieve)-np.count_nonzero(sieve)}, non zeros: {np.count_nonzero(sieve)}")
    while i < sievebound:
        if not sieve[i]:
            sum += (2*i+1)
        i += 1
    return sum


def get_collatz_sequence_len(n):
    count = 1
    orig = n
    if orig % 10000 == 0:
        print(orig, end='\r')
    while n > 1:
        if n%2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        count += 1
    return orig, count


def get_collatz_sequence_length(n, print_=False):
    count = 1
    while n > 1:
        if print_:
            print(n, end=' -> ')
        if n%2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        count += 1
    if print_:
        print(n)
    return count


def fac(n):
    if n == 0:
        return 1
    if n > 1:
        return n * fac(n-1)
    return n


def binom_coeff(n, k):
    return fac(n)/(fac(k)*fac(n-k))


def get_proper_divisors(n, include_self=False):
    if n < 2:
        return [1]
    factors = get_prime_factors(n)
    if n in factors:
        factors.remove(n)
    if n > 1 and 1 not in factors:
        proper_divisors = factors + [1]
    else:
        proper_divisors = factors
    for factor in factors:
        i = factor
        while i <= n//2:
            if i not in proper_divisors and n % i == 0:
                proper_divisors.append(i)
            i += factor
    if include_self and n not in proper_divisors:
        proper_divisors.append(n)
    return sorted(proper_divisors)


def fibo(curr_0, curr_1, limiter=None):
    new = curr_0 + curr_1

    if limiter is not None and limiter(new, curr_0, curr_1):
        return

    fibo(curr_1, new, limiter)


def is_palindrome(n):
    n = str(n)
    middle = len(n) // 2
    if not is_even(len(n)):
        n = n[:middle] + n[middle + 1:]

    # split string in two lists, reverse 2nd list and check if lists are same
    n_left, n_right = n[:middle], ''.join(reversed(n[middle:]))
    if n_left == n_right:
        return True
    return False


def is_pandigital(n):
    n = str(n)
    available = [c for c in '123456789'[:len(n)]]
    for char in str(n):
        if char in available:
            available.remove(char)
        else:
            return False
    return True if not available else False

