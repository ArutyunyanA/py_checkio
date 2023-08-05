def correct_capital(line: str) -> bool:
    return line in (line.upper(), line.lower(), line.capitalize())


print("Example:")
print(correct_capital("Checkio"))

# These "asserts" are used for self-checking
assert correct_capital("Checkio") == True
assert correct_capital("CheCkio") == False
assert correct_capital("CHECKIO") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
