#!/usr/bin/env python
# coding: utf-8
import sys

for line in sys.stdin:
    if line == '42\n':
        break
    print line,

