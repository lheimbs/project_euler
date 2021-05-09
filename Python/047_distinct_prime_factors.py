import utils

N = utils.get_N() if utils.get_N() else 4

def is_cons_prms(i):
    for j in range(N):
        dprms = set(utils.get_prime_factors_faster(i+j))
        if len(dprms) != N:
            return False
    return True

i = 1
while True:
    print(i, end='\r')
    if is_cons_prms(i):
        print(i)
        break
    i += 1

