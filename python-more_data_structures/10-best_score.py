#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return 
    score_key = None
    max_value = float('-inf')
    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            score_key = key
    return score_key
