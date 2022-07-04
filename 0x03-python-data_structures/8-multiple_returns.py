#!/usr/bin/python3
def multiple_returns(sentence):
    strlen = len(sentence)
    fchar = sentence[0] if strlen > 0 else "None"
    return (strlen, fchar)
