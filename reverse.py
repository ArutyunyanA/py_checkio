"""Create and return a new Iterable that contains the same elements as the
given list items, but with the reversed order of the elements inside every
maximal strictly ascending subsequence. This function should not modify the
contents of the original list."""

from collections.abc import Iterable


def reverse_ascending(items: list[int]) -> Iterable[int]:

    result: list[int] = []
    
    for elem in items:
        if not result or elem <= result[point]:
            point = len(result)
        result.insert(point, elem)

    return result


print("Example:")
print(list(reverse_ascending([1, 2, 3, 4, 5])))

# These "asserts" are used for self-checking
assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [
    10,
    7,
    5,
    4,
    8,
    7,
    2,
    3,
    1,
]
assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([])) == []
assert list(reverse_ascending([1])) == [1]
assert list(reverse_ascending([1, 1])) == [1, 1]
assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
