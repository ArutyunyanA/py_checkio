def between_markers(text: str, begin: str, end: str) -> str:

    if begin in text:
        start_ind = text.find(begin) + len(begin)
    else:
        start_ind = 0

    if end in text:
        stop_ind = text.find(end)
    else:
        stop_ind = len(text)
    return text[start_ind:stop_ind]


print("Example:")
print(between_markers("What is >apple<", ">", "<"))

assert between_markers("What is >apple<", ">", "<") == "apple"
assert (
    between_markers("<head><title>My new site</title></head>", "<title>", "</title>")
    == "My new site"
)
assert between_markers("No[/b] hi", "[b]", "[/b]") == "No"
assert between_markers("No [b]hi", "[b]", "[/b]") == "hi"
assert between_markers("No hi", "[b]", "[/b]") == "No hi"
assert between_markers("No <hi>", ">", "<") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")
