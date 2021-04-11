import utils

def digit_nth_power(digit, n):
    summ = sum([int(i)**n for i in str(digit)])
    return summ == digit


N = utils.get_N() if utils.get_N() else 5
digi = 10
digits = []

while len(str(digi)) < N+2:
    if digit_nth_power(digi, N):
        print(digi)
        digits.append(digi)
    digi += 1

print(digits)
print(sum(digits))

