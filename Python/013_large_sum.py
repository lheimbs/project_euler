import sys
import numpy as np


if len(sys.argv) > 1 and sys.argv[1].isnumeric():
    N = int(sys.argv[1])
else:
    N = 4

numbers = []
with open('large_sum.txt', 'r') as file:
    for line in file.readlines():
        numbers.append(int(line))

sum_of_all = sum(numbers)
print(str(sum_of_all)[:10])
