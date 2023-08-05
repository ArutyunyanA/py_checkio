"""You are given a long line (a monospace font), and you have to break the line 
in order to respect a given width. Then you have to format the text according to 
the given style: "l" means you have to align the text to the left, "c" for center, 
"r" for right, and "j" means you have to justify the text. Finally, the lines of the 
output shouldn’t end with a whitespace.

If you have to put totally an odd number of spaces around a line in order to center it,
 then put even number of spaces before.

The justification rules:

since we can't always put the same number of spaces between words in a line, put 
big blocks of spaces first. For example: X---X---X--X--X--X when you have to put 12 
spaces in 5 gaps: 3-3-2-2-2;
don't justify the last line of a text.
You won't have to consider splitting a word into two parts because the given widths
are big enough.
"""


from textwrap import wrap, fill
from operator import methodcaller


def text_formatting(text: str, width: int, style: str) -> str:
    
    if style == 'l':
        return fill(text, width)
    lines = wrap(text, width)
    
    if style in 'cr':
        just = methodcaller(('rjust', 'center')[style == 'c'], width)
        return '\n'.join(map(str.rstrip, map(just, lines)))
    last = lines.pop()
    for char, line in enumerate(lines):
        miss, spaces = width - len(line), line.count(' ')

        if spaces:
            div, mod = divmod(miss, spaces)
            lines[char] = line.replace(' ', ' '*(div+1)).replace(' '*(div+1), ' '*(div+2), mod)
    
    return '\n'.join(lines + [last])


LINE = (
    "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure "
    "harum suscipit aperiam aliquam ad, perferendis ex molestias "
    "reiciendis accusantium quos, tempore sunt quod veniam, eveniet "
    "et necessitatibus mollitia. Quasi, culpa."
)
print("Example:")
print(text_formatting(LINE, 38, "l"))

# These "asserts" are used for self-checking
assert (
    text_formatting(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        38,
        "l",
    )
    == "Lorem ipsum dolor sit amet,\nconsectetur adipisicing elit. Iure\nharum suscipit aperiam aliquam ad,\nperferendis ex molestias reiciendis\naccusantium quos, tempore sunt quod\nveniam, eveniet et necessitatibus\nmollitia. Quasi, culpa."
)
assert (
    text_formatting(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        30,
        "c",
    )
    == " Lorem ipsum dolor sit amet,\nconsectetur adipisicing elit.\n Iure harum suscipit aperiam\n  aliquam ad, perferendis ex\n     molestias reiciendis\naccusantium quos, tempore sunt\n   quod veniam, eveniet et\n   necessitatibus mollitia.\n        Quasi, culpa."
)
assert (
    text_formatting(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        50,
        "r",
    )
    == "           Lorem ipsum dolor sit amet, consectetur\n     adipisicing elit. Iure harum suscipit aperiam\n   aliquam ad, perferendis ex molestias reiciendis\n       accusantium quos, tempore sunt quod veniam,\n eveniet et necessitatibus mollitia. Quasi, culpa."
)
assert (
    text_formatting(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        45,
        "j",
    )
    == "Lorem   ipsum  dolor  sit  amet,  consectetur\nadipisicing elit. Iure harum suscipit aperiam\naliquam    ad,   perferendis   ex   molestias\nreiciendis  accusantium  quos,  tempore  sunt\nquod   veniam,   eveniet   et  necessitatibus\nmollitia. Quasi, culpa."
)

print("The mission is done! Click 'Check Solution' to earn rewards!")