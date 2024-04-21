#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
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
