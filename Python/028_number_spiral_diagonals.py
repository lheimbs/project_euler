import utils


def spiral_sum(n):
    sum = counter = 1
    max_square = 2
    while True:
            if max_square >= n:
                    return sum
            for _ in range(4):
                    counter += max_square
                    sum += counter
#                    print(counter, max_square, sum)
            max_square += 2


N = utils.get_N() if utils.get_N() else 1001
print(spiral_sum(N))

