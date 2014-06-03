#!/usr/bin/env python
# coding: utf-8
from math import sqrt

# 素数
primes = [2, 3]

def is_prime(n):
    """
    素数判定
    """
    s = int(sqrt(n))+1
    for p in primes:
        if p >= s:
            break
        if n % p == 0:
            return False
    return True

# 入力される最大値までの素数判定に必要な素数を得る
num = int(sqrt(1000000000))+1
for i in range(5, num, 6):
    # 6n+5
    if is_prime(i):
        primes.append(i)
    # 6n+7
    if is_prime(i+2):
        primes.append(i+2)
    # 6n+(6,8,9,10)は2または3の倍数なので不要

# 入力
T = input()
for t in range(T):
    m, n = map(int, raw_input().split())
    m = max(m, 2)
    # 与えられた範囲の素数判定
    isPrime = [True] * (n-m+1)
    s = int(sqrt(n))+1
    for p in primes:
        if p >= s:
            break
        # 開始インデックス
        # m % p = 0の時に困るのでさらに%pする
        start = (p - (m % p)) % p
        # 初出は素数なので2回目以降まで飛ばす
        if m < 2 * p:
            start += p
        # ふるい落とし
        isPrime[start::p] = [False] * len(isPrime[start::p])

    # 素数を出力
    for i in range(m, n+1):
        if isPrime[i-m]:
            print i
    print

