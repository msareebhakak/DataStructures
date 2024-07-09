#
# Author: Sareeb Hakak
# Purpose: Learn Merge Sort
# Date: 17 March 24
#

def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)
    merge_arrays(left, right, arr)


def merge_arrays(left, right, arr):
    len_l = len(left)
    len_r = len(right)
    i = j = k = 0

    while i < len_l and j < len_r:
        if left[i] <= right[i]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len_l:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len_r:
        arr[k] = right[j]
        j += 1
        k += 1


if __name__ == '__main__':
    cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5]
    ]

    for val in cases:
        merge_sort(val)
        print(val)
