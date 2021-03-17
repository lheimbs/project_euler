#!/usr/bin/env python3

import sys
from utils import is_prime

if len(sys.argv) > 1 and sys.argv[1].isnumeric():
    NUM = int(sys.argv[1])
else:
    NUM = 10001

x = 3
i = 1
while True:
    if is_prime(x):
        i += 1
        if i == NUM:
            print(f"{x} is the {NUM} prime")
            break
    x += 1

