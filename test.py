#!/usr/bin/env python3

from math import factorial
from itertools import product, combinations as C

def C(n, k):
    return factorial(n) / ( factorial(k) * factorial(n-k) )

S = list(range(0,32))
D = list(range(0,22))

P_correct = (len(D) / len(S))**8

print(P_correct)

P_wrong = 10/32

print(P_wrong)

r = range(0,8)

total = 0.0

for i in r:
    total += (P_wrong**(i+1) * C(8, i) + 22/32 * C(8, 8-i))



print(1 - total)
