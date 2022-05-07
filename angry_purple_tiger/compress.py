from math import floor
from functools import reduce


def compress(bytes: list, target: int):
    length = len(bytes)
    if target > length:
        raise ValueError('Fewer input bytes than requested output')

    seg_size = floor(length / target)

    segments = []
    for i in range(0, seg_size * target, seg_size):
        segments.append(bytes[i:i+seg_size])

    last_seg = segments[len(segments) - 1]

    segments[len(segments) - 1] = last_seg + bytes[target * seg_size:]

    checksums = [reduce(lambda acc, curr: acc ^ curr, s) for s in segments]

    return checksums