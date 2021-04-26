from itertools import permutations
from tqdm import tqdm
import utils

len_p = 8
prims = [p for p in range(2, 18) if utils.is_prime_faster(p)]
pandigitals = [''.join(perm) for perm in permutations('0123456789')]

founds = []
for pan in tqdm(pandigitals):
    for i in range(1, 8):
        if not int(pan[i:i+3]) % prims[i-1] == 0:
            break
    else:
        founds.append(pan)

assert '1406357289' in founds
print(founds)
print(sum([int(f) for f in founds]))

