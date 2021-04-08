import sys
import utils

N = utils.get_N() if utils.get_N() else 1000

n_recursions = 2000

def limiter(new, *args):
    global counter
    counter += 1
    ndigits = len(str(new))
    if ndigits >= N:
        print(counter)
        return True
    return False


for i in range(1, 10):
    sys.setrecursionlimit(n_recursions * i)

    counter = 3
    try:
        utils.fibo(1, 2, limiter)
        sys.exit()
    except RecursionError:
        pass

