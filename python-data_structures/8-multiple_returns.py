#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "" or sentence is None:
        return (0, None)
    new_len = len(sentence)
    return (new_len, sentence[0][0])
