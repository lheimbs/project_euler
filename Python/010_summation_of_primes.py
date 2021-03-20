import sys
from time import perf_counter as timer
from utils import is_prime

if len(sys.argv) > 1 and sys.argv[1].isnumeric():
    NUM = int(sys.argv[1])
else:
    NUM = 2e6

x = 5
sum = 5
start = timer()
while x <= NUM:
    if is_prime(x):
        sum += x
    x += 2
print(f"{sum} is the sum of all primes below {NUM} in {timer()-start:0.4f} sec.")


start = timer()
while x <= NUM:
    if is_prime_faster(x):
        sum += x
    x += 2
print(f"{sum} is the sum of all primes below {NUM} in {timer()-start:0.4f} sec.")

