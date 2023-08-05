"""Your function should create a list of lists,
that represents a two-dimensional grid with the given number of rows and cols.

This grid should contain integers (int) from start to start + rows * cols - 1
in ascending order, but the elements of every odd-index row have to be listed
in descending order, so that when read in ascending order, the numbers zigzag
through the two-dimensional grid."""


def create_zigzag(rows: int, cols: int, start: int = 1) -> list[list[int]]:
#    comp_list = [sorted(range((x :=start + i * cols), x + cols), reverse= i % 2) for i in range(rows)]
    new_list = []

    for i in range(rows):
        
        x = start + i * cols
        new_list.append(sorted(range((x), x + cols), reverse= i % 2))

    return new_list


print("Example:")
print(create_zigzag(3, 5))

# These "asserts" are used for self-checking
assert create_zigzag(3, 5) == [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15]]
assert create_zigzag(5, 1) == [[1], [2], [3], [4], [5]]
assert create_zigzag(3, 3, 5) == [[5, 6, 7], [10, 9, 8], [11, 12, 13]]

print("The mission is done! Click 'Check Solution' to earn rewards!")
