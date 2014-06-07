#!/usr/bin/env python
# coding: utf-8
from math import sqrt

def sieve(m, n):
    """
    エラトステネスのふるい
    """
    # 合成数
    composites = set([1])
    for i in range(3, int(sqrt(n)) + 1, 2):
        # 次の素数を処理
        if i not in composites:
            # m - m % i: 素数iの定数倍でm以下で最大のもの
            # i ** 2:    素数iの自乗
            # 上記2数のmax未満の数については素数i未満の素数で除外済みになる
            mult = max(m - m % i, i ** 2)
            # 合成数の定数倍を記録
            while mult <= n:
                composites.add(mult)
                mult += i
    # 素数の出力
    for i in range(m, n + 1):
        if i == 2 or (i % 2 and i not in composites):
            print i

# 入力
T = input()
for t in range(T):
    m, n = map(int, raw_input().split())
    sieve(m, n)
    print

