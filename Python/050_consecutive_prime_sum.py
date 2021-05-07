import utils

MAX = int(1e6)

available_primes = [i for i in range(2, MAX//2) if utils.is_prime_faster(i)]

start = 0
sums = []
while start < len(available_primes):
    for curr in range(start, len(available_primes)+1):
        summ = sum(available_primes[start:curr])
        if summ > MAX:
            break
        if utils.is_prime_faster(summ):
            sums.append((summ, len(available_primes[start:curr])))
    start += 1
print(sorted(sums, key=lambda x: x[1])[-1])
