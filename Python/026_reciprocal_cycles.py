from decimal import Decimal, localcontext
from fractions import Fraction
from collections import namedtuple

import utils

N = utils.get_N() if utils.get_N() else 1000


def phi(m):
    res = 1
    checked_prims = set()
    prims = utils.get_prime_factors_faster(m)
    if not prims:
        prims = [m]
    for prim in prims:
        if prim not in checked_prims:
            res *= prim-1
            checked_prims.add(prim)
        else:
            res *= prim
    return res


def num_periods(n):
    if n % 2 == 0:
        n = int(n / 2)
    if n % 5 == 0:
        n = int(n / 5)
    divs = utils.get_proper_divisors(phi(n), True)
    for divsr in divs:
        if 10**divsr  % n == 1:
            return divsr
    return 0



#def get_recurring_digits(d):
#    with localcontext() as ctx:
#        ctx.prec = 1000
#        frac = Decimal(1/d)
#    print(frac)
#    #enc
#    #for digit in 



CycleNum = namedtuple('CycleNum', 'num n_fracs')
cycle_num = CycleNum(0, 0)
for i in range(1, N):
    prims = set(utils.get_prime_factors_faster(i))
    try:
        prims.remove(2)
    except KeyError:
        pass
    try:
        prims.remove(5)
    except KeyError:
        pass
    #if prims:
    n_fracs = num_periods(i)
    if n_fracs > cycle_num.n_fracs:
        cycle_num = CycleNum(i, n_fracs)
print(cycle_num)

