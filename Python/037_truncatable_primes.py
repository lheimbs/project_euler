import utils

low_primes = [2, 3, 5, 7]


def is_left_trunc(n):
    orig = n
    if '0' in str(n):
        return 0
    len_n = len(str(n)) - 1
    while n > 0:
        if not utils.is_prime_faster(n):
            return 0
        n %= 10**len_n
        len_n -= 1
    return orig


def is_right_trunc(n):
    orig = n
    ps = ('1', '3', '7', '9')
    if n > 5:
        for c in str(n)[1:]:
            if not c in ps:
                return 0
    while n > 0:
        if not utils.is_prime_faster(n):
            return 0
        n //= 10
    return orig


def is_truncatable(n):
    return n if is_left_trunc(n) > 0 and is_right_trunc(n) > 0 else 0


found = set()
i = 10
while len(found) <= 11:
    found.add(is_truncatable(i))
    i += 1

print(found)
print(sum(found))
assert 3797 in found

