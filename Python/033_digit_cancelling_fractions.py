import fractions

def is_curious(n, k):
    both = str(n) + str(k)
    if both[1] != both[2]:
        return 0, 0
    return (int(n) for n in both[0::3])

fracs = set()
for i in range(11, 98):
    for j in range(i+1, 99):
        n, k = is_curious(i, j)
        if n > 0 and k > 0:
            f = fractions.Fraction(i, j)
            if f == fractions.Fraction(n, k):
                fracs.add(f)

print(fracs)
prod = 1
for frac in fracs:
    prod *= frac

print(prod.denominator)

