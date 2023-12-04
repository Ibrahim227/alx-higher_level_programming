#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence  == []:
        sentence[0] = None
    else:
        print("Length: {:d} - First character: {}".format(len(sentence), sentence[0]))
