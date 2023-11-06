#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = 0
    if sentence is None or sentence[0] == '\n':
        return (str_len, None)
    str_len = len(sentence)
    return (str_len, sentence[0])
