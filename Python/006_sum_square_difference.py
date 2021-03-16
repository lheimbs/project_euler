#!/usr/bin/env python

import sys
from time import perf_counter as timer

if len(sys.argv) > 1 and sys.argv[1].isnumeric():
    NAT_NUMBERS = int(sys.argv[1])
else:
    NAT_NUMBERS = 100
print(f"Using {NAT_NUMBERS} numbers.")

num_range = range(1, NAT_NUMBERS+1)

quad_sum = sum([i**2 for i in num_range])
sum_quad = sum(num_range)**2
print(sum_quad, " - ", quad_sum, " = ", sum_quad - quad_sum )
