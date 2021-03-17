#!/usr/bin/env python3

numbers = range(1000)
res = sum([0 if x%3 and x%5 else x for x in numbers])

print(res)

