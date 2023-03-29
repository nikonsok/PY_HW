"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.
You may assume that that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]

_______________
Напишите функцию, которая принимает в качестве аргументов K списков и возвращает все 
возможные списки из K элементов, где первый элемент — из первого списка,
 второй — из второго и так далее. Вы можете предположить, 
 что каждый список содержит хотя бы один элемент

"""
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    if not args:
        return []
    result = []
    for fnumbs in args[0]:
        for secnumbs in combinations(*args[1:]):
            result.append([fnumbs] + secnumbs)
    return result