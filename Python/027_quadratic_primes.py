import utils

def quad_expr(a, b, n):
    return n**2 + a*n + b


def find_max_coeffs():
    n_primes = 0
    max_a_b = (0, 0)

    for a in range(-999, 1001):
        for b in range(-999, 1001):
            n = 0
            while utils.is_prime(quad_expr(a, b, n)):
                    n += 1
            if n > n_primes:
                n_primes = n
                max_a_b = (a, b)
    print(n_primes, max_a_b, max_a_b[0] * max_a_b[1])


find_max_coeffs()
