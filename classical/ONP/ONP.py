#!/usr/bin/env python
# coding: utf-8

def rpn(expr):
    """
    Reverse Polish Notation
    """
    output    = []
    operators = []
    for char in expr:
        # 変数
        if char.isalpha():
            output.append(char)
        # 演算子
        elif char in ('+', '-', '*', '/', '^'):
            operators.append(char)
        # 変数 演算子 変数の3つ組が確定した場合
        elif char == ')':
            output.append(operators.pop())
    return ''.join(output)

T = input()
for t in range(T):
    print rpn(raw_input())

