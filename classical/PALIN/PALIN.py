#!/usr/bin/env python
# coding: utf-8
import re

def palindrome(s, hoge=re.compile(r'[^9]9*$')):
    """
    与えられた文字列より大きい最小の回文を返す
    """
    length = len(s)
    # 全部が9の場合
    if all(c == '9' for c in s):
        return '1' + '0' * (len(s) - 1) + '1'
    # 回文の元になる部分を取得
    odd = length % 2
    num = s[:length/2+odd]
    # 回文生成
    pal = make_palindrome(num, odd)
    # 条件判定
    if pal > s:
        return pal
    # 条件を満たさなければ回文の種を増やす
    #return make_palindrome(str(int(num)+1), odd) # str -> int -> str はTLEになるのでNG
    # 特殊なインクリメント関数を用いる
    return make_palindrome(incr(num), odd)

def incr(n, ptn=re.compile(r'[^9]9*$')):
    """
    文字列を数値的にインクリメントする
    """
    return ptn.sub(_incr, n)

def _incr(match):
    """
    マッチオブジェクトを受け取りインクリメントして返す
    """
    c = match.group(0)
    # 先頭文字を1加算し，以下の9はすべて0にする
    # e.g. 1 -> 2, 19 -> 20, 199 -> 200, 1909 -> 09のみマッチ -> 1910
    return chr(ord(c[0])+1) + '0'*(len(c)-1)

def make_palindrome(n, odd):
    """
    与えられた整数を元に回文を生成する
    """
    # e.g. 123, odd -> 12321
    # e.g. 123, eve -> 123321
    return n + n[-odd-1::-1]

T = input()
for t in range(T):
    print palindrome(raw_input())

