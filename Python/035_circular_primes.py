import utils
from tqdm import tqdm

N = utils.get_N() if utils.get_N() else int(1e6)
n_range = range(1, N+1)
primes = [i for i in tqdm(n_range) if utils.is_prime_faster(i)]


def rotations(n):
    n = str(n)
    orig = n
    rots = []
    while True:
        n = n[-1] + n[:-1]
        rots.append(n)
        if n == orig:
            break
    return [int(r) for r in rots]


def is_cprime(rots):
    for num in rots:
        if num not in primes:
            return False
    return True


c_primes = set()
for n in tqdm(primes):
    if n in c_primes:
        continue
    rots = rotations(n)
    if is_cprime(rots):
        c_primes |= set(rots)

print(c_primes)
print(len(c_primes))

