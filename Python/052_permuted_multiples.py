
def is_same_digits(*args):
    if len(set([''.join(sorted([c for c in str(arg)])) for arg in args])) == 1:
        return True
    return False

i = 1
while True:
    muls = [i*j for j in range(1, 7)]
    if is_same_digits(*muls):
        print(i)
        break
    i += 1

