#!/usr/bin/python3
def best_score(a_dictionary):
    maxKey = 0
    if not a_dictionary:
        return None
    else:
        for k in a_dictionary:
            if a_dictionary[k] > maxKey:
                maxKey = a_dictionary[k]
        val_list = list(a_dictionary.values())
        key_list = list(a_dictionary.keys())
        val = val_list.index(maxKey)
        return key_list[val]
