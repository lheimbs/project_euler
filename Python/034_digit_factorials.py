import utils

factorials = {i: utils.fac(i) for i in range(10)}

def is_factorial(n):
    summ = sum([factorials[int(digit)] for digit in str(n)])
    if summ == n:
        return True
    return False


def get_max():
    num = 9
    while True:
        summ = sum([factorials[9] for digit in str(num)])
        if num > summ:
            break
        num = int(str(num) + '9')
    return len(str(num)) * factorials[9]


i = 10
nums = []
maxx = get_max()
print('max', maxx)
while i < maxx:
    if is_factorial(i):
        print(i)
        nums.append(i)
    i += 1

print(nums)
print(sum(nums))

