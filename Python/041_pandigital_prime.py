import utils


def panprim():
    pnd_prms = []
    for i in range(5,9):
        for num in [int(''.join(p)) for p in itertools.permutations('123456789', i)]:
            if utils.is_prime_faster(num) and utils.is_pandigital(num):
                pnd_prms.append(num)
    print(max(pnd_prms))


panprim()
