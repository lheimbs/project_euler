#!/usr/bin/env python3
import utils

MAX = 4e6
res = 0


def is_even(x):
    return not x%2


def limiter(new, curr_0, curr_1):
    global res
    if is_even(curr_1):
        res += curr_1

    if new > MAX:
        print(res)
        return True
    return False


utils.fibo(1,2, limiter=limiter)

