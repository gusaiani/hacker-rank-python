# https://www.hackerrank.com/challenges/simple-array-sum/problem
from functools import reduce

def solve(ar):
    return reduce((lambda x, y: x + y), ar)

def solve_with_sum(ar):
    return sum(ar)

def test_simple_array_sum():
    arr = [1, 2, 3, 4, 10, 12]
    assert solve(arr) == 32
    assert solve_with_sum(arr) == 32
