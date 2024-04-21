#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    keys = [0]
    for i in range(0, len(boxes)):
        if i in keys:
            keys.extend(boxes[i])
            for j in boxes[i]:
                keys.extend(boxes[j])
        else:
            return False
    return True
