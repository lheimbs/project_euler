import utils

MAX = 28123

def get_abundant_numbers():
    abundants = []
    for n in range(1, MAX+1):
        if n % 1000 == 0:
            print(n, end='\r')
        sum_ = sum(utils.get_proper_divisors(n))
        if sum_ > n:
            abundants.append(n)
    return abundants


abundants = get_abundant_numbers()
sums = set()
for i in abundants:
    for j in abundants:
        sums.add(i+j)

non_abunds = {i for i in range(1, MAX+1)} - sums
print(sum(non_abunds))

