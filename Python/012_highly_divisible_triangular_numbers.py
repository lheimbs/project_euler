import sys
import multiprocessing
from time import perf_counter as timer
from utils import get_prime_factors


def get_num_factors_for_prime(n, prim):
    counter = 0
    while n%prim == 0:
        counter += 1
        n /= prim
    return counter


def get_num_factors(n):
    # very slow but works ¯\_(ツ)_/¯
    factors = get_prime_factors(n)
    num_facs = len(factors)
    for prim in factors:
        fac = prim * 2
        while fac <= n**(1/2):
            if n%fac == 0 and fac not in factors:
                num_facs += 1
                factors.append(fac)
            fac += prim
    return num_facs, factors


def get_max_divisors(N, start, step):
    # get triangle numbers starting from N
    num = 0
    facs = None
    i = start
    while True:
        if i%1000 == 0:
            print(i, end='\r')
        tri = ((i + 1) * i) / 2
        num, _ = get_num_factors(tri)
        if num > N/2:
            print(f"{tri} is the first triangle number n=({i}) to have more than {N} factors ({num})")
            break
        i += step
    return True


def get_stolen(N):
    # from https://www.xarg.org/puzzle/project-euler/problem-12/
    def tau(num):
        n = num
        i = 2
        p = 1
        if num == 1:
            return 1
        while i*i <= n:
            c = 1
            while n%i == 0:
                n /= i
                c += 1
            i += 1
            p *= c
        if n == num or n > 1:
            p *= 1+1
        return p
    n = 1
    d = 1
    while tau(d) <= N:
        n+=1
        d+=n
    print("stolen: ", d)

#print(sorted(get_factors(N)))
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].isnumeric():
        N = int(sys.argv[1])
    else:
        N = 500
    if len(sys.argv) > 2:
        start = int(sys.argv[2])
    else:
        start = N
    if len(sys.argv) > 3:
        step = int(sys.argv[3])
    else:
        step = 1
    # does not work :(
    get_stolen(N)
    get_max_divisors(N, start, step)

