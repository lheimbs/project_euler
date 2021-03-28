from num2words import num2words
import utils
N = utils.get_N() if utils.get_N() else 1000

count = 0
for i in range(1, N+1):
    num = num2words(i).replace(' ', '').replace('-', '')
    print(i, num)
    count += len(num)

print(count)

