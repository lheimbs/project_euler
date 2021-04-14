from tqdm import tqdm

def is_pandigital(*args):
    available = [c for c in '123456789']
    for num in args:
        for char in str(num):
            if char in available:
                available.remove(char)
            else:
                return False
    return True if not available else False


def is_pdgtl(*args):
    available = '123456789'
    nums = []
    for num in args:
        nums += [char for char in str(num)]
    if available == ''.join(sorted(nums)):
        return True
    return False


def bruteforce():
    MAX = 100000
    found = set()
    for i in tqdm(range(1, MAX)):
        for j in range(i, MAX):
            product = i * j
            if len(''.join((str(i), str(j), str(product)))) > 9:
                break
            if is_pdgtl(i, j, product):
                found.add((i, j, product))
    return found


founds = bruteforce()
from pprint import pprint
pprint(founds)
print(sum({f[2] for f in founds}))

