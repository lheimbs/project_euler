#!/usr/bin/env python

import sys
from time import perf_counter as timer

MAX_DIVISOR = 20
divisors = range(11 if MAX_DIVISOR < 11 else 2, MAX_DIVISOR)


def is_digit_sum_divisible(str_z, divisor):
    if sum([int(j) for j in str_z])%divisor == 0:
        return True
    return False


def test_brute_force(x, *args):
    global divisors
    for div in divisors:
        if not x%div == 0:
            return False
    #if all([x%divisor==0 for divisor in divisors]):
    #    return True
    return True


def test_long_brute_force(x, *args):
    if all([x%divisor==0 for divisor in divisors]):
        return True
    return False


def delbart(t,n):
    # https://projecteuler.net/action=redirect;post_id=1441
    if n > 0:
        if not (t%n):
            if delbart(t, n-1):
                return True
            else:
                return False
        else:
            return False
    else:
        return True


if __name__ == '__main__':
    if len(sys.argv) > 1:
        MAX_DIVISOR = int(sys.argv[1])
    divisors = range(11 if MAX_DIVISOR > 19 else 2, MAX_DIVISOR)
    funcs = {'brute force': test_brute_force, 'bjoernes': delbart, 'long brute force': test_long_brute_force}

    for name, func in funcs.items():
        z = MAX_DIVISOR
        if MAX_DIVISOR == 20 and not func(232792560, MAX_DIVISOR):
            sys.exit(f"{name} does not work")

        start = timer()
        while not func(z, MAX_DIVISOR):
            z+=MAX_DIVISOR
        end = timer()
        print(z)
        print(f"{name} took {end - start:0.4f} seconds")

