import sys
import utils

N = utils.get_N() if utils.get_N() else 2

my_range = list(range(N+1))
counter = 0
last_perm = None

def range_without_n(n, old_range):
    new_range = old_range.copy()
    new_range.remove(n)
    return new_range


def permutate(objects, *args):
    global counter, last_perm
    if counter >= 1e6:
#        print(last_perm)
        sys.exit(last_perm)

    args = list(args)
    for n in objects:
        try:
            args.remove(n)
        except ValueError:
            pass

    if len(objects) > 1:
        for n in objects:
            args.append(n)
            permutate(range_without_n(n, objects), *args)
    else:
        counter += 1
        n = objects[0]
        last_perm = f"{''.join([str(i) for i in args])}{n} {counter}"
        print(last_perm, end='\r')


permutate(my_range)

