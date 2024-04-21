#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    if type(boxes) is not list or len(boxes) == 0:
        return False
    keys = [0]
    for i in range(0, len(boxes)):
        if i in keys:
            keys.extend(boxes[i])
            for j in boxes[i]:
                if j < len(boxes):
                    keys.extend(boxes[j])

        else:
            return False
    return True

if __name__ == "__main__":
    boxes = []

    keys = []
    for n in range(1, 1000):
        keys = []
        for m in range(1, 1000):
            keys.append(m)
        boxes.append(keys)

    print(canUnlockAll(boxes))