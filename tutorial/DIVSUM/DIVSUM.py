#!/usr/bin/env python
# coding: utf-8
from math import sqrt

def divsum(n):
    sqrt_n = int(sqrt(n)) + 1
    ds = 1
    for i in range(2, sqrt_n):
        if n % i == 0:
            ds += i
            ds += n / i
    return ds

T = input()
for t in range(T):
    n = input()
    print divsum(n)

