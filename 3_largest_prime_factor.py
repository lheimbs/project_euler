#!/usr/bin/env python3

from timeit import default_timer as timer


def prime_factors(x):
    res=[]
    for i in range(2,x//2):
        if x%i==0 and is_prime(i):
            res.append(i)
    return res


def is_prime(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0 or x % 3 == 0:
        return False
    else:
        for i in range(5, round(x**(1/2)), 6):
            if x % i == 0 or x % (i + 2) == 0:
                return False
    return True


if __name__ == "__main__":
    start = timer()
    print(prime_factors(13195))
    end = timer()
    start_3 = timer()
    for i in range(100000000):
        if is_prime(i):
            print(i)
    end_3 = timer()
    print(f"Elapsed Time: {end_3 - start_3}")
    input("Continue with <Enter>...")
    start2 = timer()
    print(max(prime_factors(600851475143)))
    end2 = timer()
    print(f"Elapsed Time for Result 2: {end2 - start2}")
    print(f"Total Time: {end2 - start}")
