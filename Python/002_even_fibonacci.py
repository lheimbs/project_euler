#!/usr/bin/env python3

MAX = 4e6
res = 0

def is_even(x):
    return not x%2

def fibo(curr_0, curr_1):
    global res
    new = curr_0 + curr_1
    # print("new", new, "res", res)
    if is_even(curr_1):
        res+=curr_1

    if new > MAX:
        print(res)
        return

    fibo(curr_1, new)

fibo(1,2)
