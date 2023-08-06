"""
You are given a list of integers. Your function should return the number of elements,
which are not at their places as if the list would be sorted ascending. For example, 
for the sequence [1, 1, 4, 2, 1, 3] the result is 3, since elements at 
indexes 2, 4, 5 (remember about 0-based indexing in Python) are not at their places 
as in the same sequence sorted ascending - [1, 1, 1, 2, 3, 4].

"""

def not_order(data: list[int]) -> int:
    sort_list = [char for ind, char in zip(data, sorted(data)) if ind != char]
    res = [sort_list.count(x) for x in sort_list]
    return sum(res)


print("Example:")
print(not_order([1, 1, 4, 2, 1, 3]))

# These "asserts" are used for self-checking
assert not_order([1, 1, 4, 2, 1, 3]) == 3
assert not_order([]) == 0
assert not_order([1, 1, 1, 1, 1]) == 0
assert not_order([1, 2, 3, 4, 5]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")