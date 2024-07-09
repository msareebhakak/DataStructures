#
# Author: Sareeb Hakak
# Purpose: Practice arrays
# Date: 16 March 24
#
from enum import Enum


# print a 2D array in circular order

class Direction(Enum):
    RIGHT = 0
    BOTTOM = 1
    LEFT = 2
    UP = 3


def print_spiral(arr):
    rows = len(arr)
    cols = len(arr[0])
    flat = []

    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1
    direction = Direction.RIGHT

    while top <= bottom and left <= right:

        if direction == Direction.RIGHT:
            for i in range(left, right + 1):
                flat.append(arr[top][i])
            top += 1
            direction = Direction.BOTTOM

        elif direction == Direction.BOTTOM:
            for i in range(top, bottom + 1):
                flat.append(arr[i][right])
            right -= 1
            direction = Direction.LEFT

        elif direction == Direction.LEFT:
            for i in range(right, left - 1, -1):
                flat.append(arr[bottom][i])
            bottom -= 1
            direction = Direction.UP

        elif direction == Direction.UP:
            for i in range(bottom, top - 1, -1):
                flat.append(arr[i][left])
            left += 1
            direction = Direction.RIGHT

    return flat


# kadane's algorithm
# works if all values in arr are not negative
def maximum_sub_array(arr):
    ans = 0
    add = 0

    if len(arr) == 1:
        return arr[0]

    for i in arr:
        if add + arr[i] > 0:
            add += arr[i]
        else:
            add = 0
        ans = max(ans, add)
    return ans


if __name__ == '__main__':
    val = [[2, 4, 6, 8], [5, 9, 12, 16], [2, 11, 5, 9], [3, 2, 1, 8]]
    print(print_spiral(val))
