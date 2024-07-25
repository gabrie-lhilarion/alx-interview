#!/usr/bin/python3

def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0:
                continue

            # For 1 byte character, continue to next byte
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the next byte is of the form 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False
        
        num_bytes -= 1

    return num_bytes == 0
