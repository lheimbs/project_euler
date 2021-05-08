import utils

def is_permutation(*args):
    if len(args) < 2:
        return False
    sorted_args = set()
    for arg in args:
        sorted_args.add(''.join(sorted([c for c in str(arg)])))
    if len(sorted_args) == 1:
        return True
    return False


fourdprimes = [i for i in range(1000, 10000) if utils.is_prime_faster(i)]
for i, prime in enumerate(fourdprimes):
    for nextp in fourdprimes[i+1:]:
        step = nextp - prime
        if nextp + step > 9999:
            break
        if nextp + step in fourdprimes and is_permutation(prime, nextp, nextp + step):
            print(prime, nextp, nextp + step, step)

