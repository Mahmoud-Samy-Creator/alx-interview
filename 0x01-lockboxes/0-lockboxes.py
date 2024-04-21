#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """
    Function that checks with boolean value if the list type and
    length to invoke two for iterations one to traverse the list
    and the other to compaer if key is idx or not in order to open
    """
    if type(boxes) is not list or len(boxes) == 0:
        return False
    keys = []
    keys.extend(boxes[0])
    for i in range(1, len(boxes)):
        if i in keys:
            keys.extend(boxes[i])
            for j in boxes[i]:
                if j < len(boxes):
                    keys.extend(boxes[j])
        else:
            return False
    return True
