import utils
N = utils.get_N() if utils.get_N() else 1000

res = 2**N
print(f"2^{N}={res} and the sum of its digits is: {sum([int(i) for i in str(res)])}")

