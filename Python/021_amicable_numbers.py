import utils
N = utils.get_N() if utils.get_N() else 10000


def d(n):
    return sum(utils.get_proper_divisors(n))

def is_amicable(a):
    b = d(a)
    if b != a and d(b) == a:
        return b
    return 0


amicables_sum = 0
amicables = []
for n in range(1, N):
    b = is_amicable(n)
    if b and n not in amicables and b not in amicables:
        print(n, b)
        amicables.append(n)
        amicables.append(b)

print(sum(amicables))

