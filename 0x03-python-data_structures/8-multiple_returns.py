#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence[0] == None:
        return None
    return (len(sentence), sentence[0])
