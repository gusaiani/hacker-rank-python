# https://www.hackerrank.com/challenges/diagonal-difference/problem
import math
from functools import reduce

def solve(ar):
    dimension = int(math.sqrt(len(ar)))
    d1 = d2 = 0

    for x in range(0, dimension):
        index = (dimension * x) + x
        d1 += ar[index]

    for x in range(0, dimension):
        index = (dimension * x) + (dimension - 1 - x)
        d2 += ar[index]

    return abs(d1 - d2)

def test_simple_array_sum():
    arr = [1, 2, 3, 4, 5, 6, 9, 8, 9]
    assert solve(arr) == 2
