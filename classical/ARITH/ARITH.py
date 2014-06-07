#!/usr/bin/env python
# coding: utf-8
import re

ptn = re.compile(r'(\d+)([-\+\*])(\d+)')

def print_mul(x, y):
    """
    乗算の出力
    """
    ix = int(x)
    iy = int(y)
    ixy = ix * iy
    n_ixy = len(str(ixy))
    n = max(n_ixy, len(y)+1)
    print '%%%ds' % n % x
    print '%%%ds' % n % ('*'+y)
    print '%%%ds' % n % ('-'*(max(len(str(ix*int(y[-1]))), len(y)+1)))
    for i, d in enumerate(y[::-1]):
        z = ix * int(d)
        print '%%%dd' % (n-i) % z
    if i != 0:
        print '%%%ds' % n % ('-'*n_ixy)
        print '%%%dd' % n % ixy
    print

def print_add(x, y):
    """
    加算の出力
    """
    sum = int(x) + int(y)
    n_sum = len(str(sum))
    n = max(n_sum, len(y)+1)
    print '%%%ds' % n % x
    print '%%%ds' % n % ('+'+y)
    print '-' * n
    print '%%%ds' % n % sum
    print

def print_min(x, y):
    """
    減算の出力
    """
    sum = int(x)-int(y)
    n_sum = len(str(sum))
    n = max(len(x), len(y)+1)
    print '%%%ds' % n % x
    print '%%%ds' % n % ('-'+y)
    print '%%%ds' % n % ('-'*max(n_sum, len(y)+1))
    print '%%%ds' % n % (sum)
    print

T = input()
for t in range(T):
    line = raw_input()
    m = ptn.match(line)
    x = m.group(1)
    o = m.group(2)
    y = m.group(3)
    if o == '*':
        print_mul(x, y)
    elif o == '+':
        print_add(x, y)
    else:
        print_min(x, y)

