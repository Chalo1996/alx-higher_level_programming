#!/usr/bin/python3
def text_indentation(text):
    """

    prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: the string to be scanned

    Return:
        The return. None

    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    separatorList = [".", "?", ":"]

    bit = 0

    for ch in text:
        if bit == 0 and ch == " ":
            continue
        else:
            bit = 1
        if bit == 1:
            if ch in separatorList:
                print(ch)
                print()
                bit = 0
            else:
                print(ch, end="")
