#!/usr/bin/env python3

from timeit import default_timer as timer
from utils import is_prime

def primefactors(n):
    factors = []
    initial = n
    while initial > 1:
        i = 2
        found = False
        while i*i <= initial and not found:
            if initial % i == 0:
                found = True
                prime = i
            else:
                i+=1

        if not found:
            prime = initial

        factors.append(prime)
        initial = initial // prime
    return factors


def prime_factors(x):
    res=[]
    if is_prime(x):
        print("prime", x)
        res.append(x)
        return res

    for i in range(2,x//2):
        if x%i==0 and is_prime(i):
            res.append(i)
            res+=prime_factors(x//i)
            break
    return res


if __name__ == "__main__":
    TEST_NUM = 13195
    NUM = 600851475143

    start = timer()
    fs = prime_factors(TEST_NUM)
    end = timer()
    print(max(fs), fs)
    print(f"Elapsed Time: {end - start}")

    start2 = timer()
    fs = prime_factors(NUM)
    end = timer()
    print(max(fs), fs)
    print(f"Elapsed Time 2: {end - start2}")

    start2 = timer()
    fs = primefactors(TEST_NUM)
    end = timer()
    print(max(fs), fs)
    print(f"Elapsed Time 3: {end - start2}")

    start2 = timer()
    fs = primefactors(NUM)
    end = timer()
    print(max(fs), fs)
    print(f"Elapsed Time 4: {end - start2}")

    print(f"Total Time: {end - start}")
