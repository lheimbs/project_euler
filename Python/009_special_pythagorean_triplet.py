import sys
from tqdm import tqdm

if len(sys.argv) > 1 and sys.argv[1].isnumeric():
    n = int(sys.argv[1])
else:
    n = 1000

def assert_triplet(a, b, c):
    order = a < b < c
    prod = a**2 + b**2 == c**2
    if order and prod:
        return True
    return False

def get_triplet_for_sum(n):
    for i in tqdm(range(1,n//3)):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if assert_triplet(i, j, k) and i+j+k == n:
                    print(f"{i}+{j}+{k} = {n}; prod = {i*j*k}.")
                    return i, j, k

get_triplet_for_sum(n)
