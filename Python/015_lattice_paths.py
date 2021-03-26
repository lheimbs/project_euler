import sys
from utils import binom_coeff

if len(sys.argv) > 1 and sys.argv[1].isnumeric():
    N = int(sys.argv[1])
else:
    N = 20

def lattice_paths(n):
    return binom_coeff(2*n, n)


if __name__ == '__main__':
    print(lattice_paths(N))

