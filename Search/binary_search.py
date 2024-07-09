#
# Author: Sareeb Hakak
# Purpose: Learn binary search
# Date: 03 March 24
#
import time
import numpy as np


def linear_search(vals, num):
    for count, val in enumerate(vals):
        if val == num:
            return count
    return -1


def binary_search(vals, num):
    left_index = 0
    right_index = len(vals) - 1

    while left_index <= right_index:
        mid_index = int((left_index + right_index) / 2)
        mid_num = vals[mid_index]

        if mid_num == num:
            return mid_index

        if mid_num < num:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1


def binary_search_occurrence(vals, num, search_first):
    left_index = 0
    right_index = len(vals) - 1
    result = -1

    while left_index <= right_index:
        mid_index = int((left_index + right_index) / 2)
        mid_num = vals[mid_index]

        if mid_num == num:
            result = mid_index
            if search_first:
                right_index = mid_index - 1
            else:
                left_index = mid_index + 1
        elif mid_num < num:  # Update the condition here
            left_index = mid_index + 1
        elif mid_num > num:
            right_index = mid_index - 1

    return result


def find_count(array, num):
    # this method uses the first and last occurrence of an element
    # and then for sorted array [first:last] would be the elements
    first_index = binary_search_occurrence(array, num, search_first=True)
    last_index = binary_search_occurrence(array, num, search_first=False)
    if first_index == -1:
        return -1
    else:
        return last_index - first_index + 1


def binary_search_re(vals, num, left_index=0, right_index=None):
    if right_index is None:
        right_index = len(vals) - 1

    mid_index = int((left_index + right_index) / 2)
    mid_num = vals[mid_index]

    if left_index > right_index:
        return -1

    if mid_num == num:
        return mid_index
    elif mid_num < num:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_re(vals, num, left_index, right_index)


def find_smallest(vals):
    left = 0
    right = len(vals) - 1

    # If the array is already sorted and not rotated, return the first element
    if vals[left] <= vals[right]:
        return left

    while left < right:
        mid = (left + right) // 2

        # Check if the middle element is greater than the last element
        if vals[mid] > vals[right]:
            # Smallest element is in the right half
            left = mid + 1
        else:
            # Smallest element is in the left half or is the middle element
            right = mid

    return left


def circular_array_search(vals, x):
    left = 0
    right = len(vals) - 1

    while left <= right:
        mid = (left + right) // 2

        if x == vals[mid]:
            return mid
        # check which subarray is sorted
        if vals[mid] <= vals[right]:
            # right half is sorted, check for x within limits
            if vals[mid] < x <= vals[right]:
                left = mid + 1
            else:
                right = mid - 1
        elif vals[left] <= vals[mid]:
            if vals[left] <= x < vals[mid]:
                right = mid - 1
            else:
                left = mid + 1

    return -1


if __name__ == '__main__':
    elements = np.arange(1000000000)
    start_t = time.time()
    print(linear_search(elements, 999999999))
    print(f'Time taken for linear search {time.time() - start_t} s')
    start_ = time.time()
    print(binary_search_re(elements, 999999999))
    print(f'Time taken for binary search {time.time() - start_} s')

    # first = [2, 4, 10, 10, 10, 10, 18, 20]
    # print(binary_search_occurrence(first, 10, search_first=True))  # answer 2
    # print(binary_search_occurrence(first, 10, search_first=False))
    # print(find_count(first, 1))
    #
    # arr = [5, 6, 7, 1, 2, 3, 4]
    # print("The array has been rotated circularly by:", find_smallest(arr))
    #
    # print(circular_array_search(arr, 5))
    