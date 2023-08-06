"""
Joe Palooka has fat fingers, so he always hits the “Caps Lock” key whenever 
he actually intends to hit the key “a” by itself. (When Joe tries to type in 
some accented version of “a” that needs more keystrokes to conjure the accents, 
he is more careful in the presence of such raffinate characters ([Shift] + [a]) 
and will press the keys correctly). Compute and return the result of having Joe type 
in the given text. The “Caps Lock” key affects only the letter keys from “a” to “z” , 
and has no effect on the other keys or characters. “Caps Lock” key is assumed to be 
initially off.

def caps_lock(text: str) -> str:
    
    def characters():

        caps = False
        for char in text:
            if char == 'a':
                caps = not caps
            else: 
                yield char.upper() if caps else char

    return ''.join(characters())
    
"""

def caps_lock(text: str) -> str:

    result = text.split('a')
    for char in range(1, len(result), 2):
        result[char] = result[char].upper()
    return ''.join(result)

#    return ''.join((char, char.upper())[ind % 2] for ind, char in enumerate(text.split('a')))


print("Example:")
print(caps_lock("Why are you asking me that?"))

# These "asserts" are used for self-checking
assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"

print("The mission is done! Click 'Check Solution' to earn rewards!")