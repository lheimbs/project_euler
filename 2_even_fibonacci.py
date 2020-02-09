#!/usr/bin/env python3

MAX = 4e6

def fib(x=None):
    if not x:
        print("array is empty")
        x=[0]
    elif len(x) == 1:
        print("array has only one entry")
        x.append(1)
    elif x[-1] > MAX:
        print("Max value reached ",x[-1])
        return x
    else:
        x.append(x[-2]+x[-1])
    x = fib(x)
    return x 

print(sum([0 if x%2 else x for x in fib()]))
