#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    best = max(a_dictionary.items(), key=lambda item: item[1], default=None)
    return (best[0])
