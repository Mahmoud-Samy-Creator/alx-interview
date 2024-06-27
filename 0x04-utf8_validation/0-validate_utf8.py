#!/usr/bin/python3

"""
UTF-validation function
"""


def validUTF8(data):
    """
    Validate if a list of integers represents a valid UTF-8 encoding.

    Args:
    - data: A list of integers representing bytes.

    Returns:
    - True if the list represents a valid UTF-8 encoding, False otherwise.
    """

    # Edge case: if data is empty, return False
    if not data:
        return False

    # Validate each byte in data
    for num in data:
        # Check if num is a valid byte value (0-255)
        if num < 0 or num > 255:
            return False

    bitList = []

    # Convert each number to its 8-bit binary representation
    for num in data:
        bitList.append(bin(num).replace("0b", "").zfill(8))

    # Iterate through each binary representation
    for i in range(len(bitList)):
        if bitList[i][0] == '0':
            # Single byte sequence (0xxxxxxx)
            continue
        else:
            # Multi-byte sequence: Determine number of bytes
            count = 0
            for x in range(len(bitList[i])):
                if bitList[i][x] == '1':
                    count += 1
                else:
                    break
            # Check continuation bytes
            for c in range(1, count):
                if bitList[i + c][0:2] != '10':
                    return False

    # All checks passed, return True indicating valid UTF-8
    return True
