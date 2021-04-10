import utils

def distinct_powers(n):
    pwrs = set()
    for i in range(2, n+1):
        for j in range(2, n+1):
            pwrs.add(i**j)
    return pwrs


if __name__ == '__main__':
    N = utils.get_N() if utils.get_N() else 100
    pwrs = distinct_powers(N)
    print(len(pwrs))

