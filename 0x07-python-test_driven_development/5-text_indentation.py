#!/usr/bin/python3
"""A module that defines a function text_indentation
that prints a text with 2 new lines after each of these
characters: ., ?, and :
"""


def text_indentation(text):
    """A function that prints a text with 2 new lines after
    each of these characters: ., ?, and :

    Args:
        text (str): Text to be parsed.

    Raises:
        TypeError: Raised if text is not a string
    """

    new_text = ""
    skip = False
    c = 0
    if text is None or not isinstance(text, str):
        raise TypeError("text must be a string")
    while c in range(len(text)):
        if text[c] != ' ':
            break
    for c in range(len(text)):
        if text[c] == ' ' and skip is False and c < len(text) - 1 and \
           text[c + 1] != '.' and text[c + 1] != '?' and text[c + 1] != ':':
            new_text += text[c]
        if text[c] == '.' or text[c] == '?' or text[c] == ':':
            new_text += text[c] + '\n\n'
            if c < len(text) - 1 and text[c + 1] == ' ':
                skip = True
                c += 1
            continue
        if text[c] != ' ':
            new_text += text[c]
            skip = False
    print(new_text)
