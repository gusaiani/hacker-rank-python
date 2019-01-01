# https://www.hackerrank.com/challenges/designer-pdf-viewer
from functools import reduce

def get_highest(char, highest):
    return 3

def solve(character_heights, word):
    highest = 0
    word_length = 0

    for char in list(word):
        height = character_heights[ord(char) - 97]
        word_length = word_length + 1

        if height > highest:
            highest = height

    return highest * word_length

def test_simple_array_sum():
    character_heights = [
        1, 3, 1, 3, 1, 4, 1, 3, 2,
        5, 5, 5, 5, 5, 5, 5, 5, 5,
        5, 5, 5, 5, 5, 5, 5, 5
    ]

    word = 'abc'

    assert solve(character_heights, word) == 9

    character_heights = [
        1, 3, 1, 3, 1, 4, 1, 3, 2,
        5, 5, 5, 5, 5, 5, 5, 5, 5,
        5, 5, 5, 5, 5, 5, 5, 7
    ]

    word = 'zaba'

