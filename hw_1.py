"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List, Tuple
from random import randint
from collections import Counter

# List = [randint(1,50) for i in range (150)]
LISTS = [
    ([2, 2, 1, 1, 1, 2, 2], (2, 1)), 
    ([3, 2, 3], (3, 2)),
    ([3, 3, 2, 2, 3, 3, 1], (3, 1))
]

def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    cnt = Counter(inp)
    max_key = max(cnt, key=cnt.get)
    min_key = min(cnt, key=cnt.get)
    return max_key, min_key

