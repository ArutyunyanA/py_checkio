def column_number(name):
    
    count = 0

    for c, k in enumerate(name[::-1]):
        count += (ord(k) - 64) * (26 ** c)
    return name + str(count) 


print("Example:")
print(column_number("AA"))

# These "asserts" are used for self-checking
print(column_number("A"))
print(column_number("Z"))
print(column_number("AB"))
print(column_number("ZY"))

print("The first mission is done! Click 'Check' to earn cool rewards!")
