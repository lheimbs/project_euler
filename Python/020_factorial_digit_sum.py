import utils

N = utils.get_N() if utils.get_N() else 100

num = utils.fac(N)
print(sum([int(digit) for digit in str(num)]))

