import sys
import multiprocessing


def get_collatz_sequence_len(n):
    count = 1
    orig = n
    if orig % 10000 == 0:
        print(orig, end='\r')
    while n > 1:
        if n%2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        count += 1
    return orig, count


def brute_force(N):
    with multiprocessing.Pool() as p:
        res = p.map(get_collatz_sequence_len, range(1, N))
    print(sorted(res, key=lambda x: x[1])[-1])


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].isnumeric():
        N = int(sys.argv[1])
    else:
        N = int(1e6)

    brute_force(N)

