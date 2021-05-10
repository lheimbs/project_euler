#import utils
#from tqdm import tqdm
import math

p = lambda n: int(n*(3*n-1)/2)
p_inv = lambda n: (math.sqrt(24*n+1)+1)/6

def is_pentagonal(n):
    return p_inv(n).is_integer()

k = 2
found = False
while not found:
    pk = p(k)
    j = k - 1
    while j > 0:
        pj = p(j)
        if is_pentagonal(pk+pj) and is_pentagonal(pk-pj):
            print(j, k, abs(pj-pk))
            found = True
            break
        j -= 1
    k += 1

