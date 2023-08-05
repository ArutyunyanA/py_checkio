"""
Your task is to encrypt the text message using the Morse code . 
The input text will consist of letters (in uppercase and lowercase), 
numbers and whitespaces. There won't be any special characters ('&', '?', '#' etc.) 
You need to use 3 spaces between words and 1 space between each letter of each word.
"""


MORSE = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def morse_encoder(text: str) -> str:
    return ' '.join(MORSE.get(char, ' ') for char in text.lower())


print("Example:")
print(morse_encoder("some text"))

assert morse_encoder("some text") == "... --- -- .   - . -..- -"
assert (
    morse_encoder("I was born in 1990")
    == "..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")

