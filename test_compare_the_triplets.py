# https://www.hackerrank.com/challenges/compare-the-triplets/problem
from functools import reduce

def solve(array1, array2):
    array1_total = 0
    array2_total = 0

    for i in range(len(array1)):
        if array1[i] > array2[i]:
            array1_total += 1
        if array2[i] > array1[i]:
            array2_total += 1

    return f"{array1_total} {array2_total}"

def solve2(array1, array2):
    sum1 = sum(a > b for a, b in zip(array1, array2))
    sum2 = sum(a < b for a, b in zip(array1, array2))
    return f"{sum1} {sum2}"

def test_simple_array_sum():
    array1 = [5, 6, 7]
    array2 = [3, 6, 10]
    assert solve(array1, array2) == '1 1'
    assert solve2(array1, array2) == '1 1'

    array1 = [17, 28, 30]
    array2 = [99, 16, 8]
    assert solve(array1, array2) == '2 1'
    assert solve2(array1, array2) == '2 1'

    array1 = [6, 8, 12]
    array2 = [7, 9, 15]
    assert solve(array1, array2) == '0 3'
    assert solve2(array1, array2) == '0 3'

