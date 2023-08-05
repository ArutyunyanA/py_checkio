def checkio(number):
	count = 1

	for x in str(number):
		if num := int(x):
			count *= num
	return count


print("Example:")
print(checkio(123405))

# These "asserts" are used for self-checking
print(checkio(123405))
print(checkio(999))
print(checkio(1000))
print(checkio(1111))

print("The mission is done! Click 'Check Solution' to earn rewards!")
