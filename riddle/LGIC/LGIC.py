#!/usr/bin/env python
# coding: utf-8
from math import factorial

def an(n):
    return factorial(n) + 2 ** n - n

n = input()
print an(n)

