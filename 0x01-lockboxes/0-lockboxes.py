#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    if type(boxes) is not list or len(boxes) == 0:
        return False
    keys = [0]
    for i in range(0, len(boxes)):
        if i in keys:
            keys.extend(boxes[i])
            for j in range(0, len(boxes[i])):
                keys.extend(boxes[j])
        else:
            return False
    return True
