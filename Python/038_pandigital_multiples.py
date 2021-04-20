from tqdm import tqdm

def get_pandigital_mul(n):
    i = 1
    results = []
    len_result = 0
    while True:
        res = str(n * i)
        len_result += len(res)
        if len_result > 9:
            break
        results += [c for c in res]
        i += 1
    if len(results) == 9:
        available = '123456789'
        if ''.join(sorted(results)) == available:
            print(n, ''.join(results))
            return int(''.join(results))
    return 0


pans = set()
for i in tqdm(range(1, int(int('9'*9)**0.5))):
    pan = get_pandigital_mul(i)
    if pan:
        pans.add(pan)

print(pans)
print(max(pans))

