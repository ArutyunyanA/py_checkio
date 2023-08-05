"""

Split a given text into multiline one with "\n", where each line includes number 
of words equal to the current Fibonacci number.

Here are some clarifications:

Fibonacci sequence starts from 0, 1, but the result string should include only 
non-empty lines;
in case, there are not enough words for current line - complement to proper length 
with "_"; punctuation marks are considered as a part of a previous or next word.
Let's look at the schematic example ("w" for a word):

"w w w w w w w w" -> '''w
                        w
                        w w
                        w w w
                        w _ _ _ _'''
Input: A string (str).

Output: A string (str).



from collections.abc import Iterator
def fibo_poem(text: str) -> str:

    def gen(it: Iterator[str]) -> Iterator[str]:
        
        f0, f1 = 0, 1
        while True:
            line = " ".join(next(it, "_") for _ in range(f1))
            if line.startswith("_"):
                break
            yield line
            f0, f1 = f1, f0 + f1

    it = iter(text.split())        
    return "\n".join(gen(it))

def fibo_poem(text: str) -> str:
    
    text, a, b, result = text.split()[::-1], 1, 1 , ""
    while text:
        line = (text and text.pop() or "_" for _ in range(b))
        a, b, result = a + b, a, result + ' '.join(line) + "\n"
    return result.strip()

"""



def fibo_poem(text: str) -> str:

    a, b, text, poem = 0, 1, text.split(), []
    while text:
        row, text = text[:b], text[b:]
        row.extend('_' * (b - len(row)))
        poem.append(' '.join(row))
        a, b = b, a + b
    return '\n'.join(poem)

   




print("Example:")
print(fibo_poem("Zen of Python"))

# These "asserts" are used for self-checking
assert fibo_poem("") == ""
assert fibo_poem("Django framework") == "Django\nframework"
assert fibo_poem("Zen of Python") == "Zen\nof\nPython _"
assert (
    fibo_poem("There are three kinds of lies: Lies, damned lies, and the benchmarks.")
    == "There\nare\nthree kinds\nof lies: Lies,\ndamned lies, and the benchmarks."
)

print("The mission is done! Click 'Check Solution' to earn rewards!")



