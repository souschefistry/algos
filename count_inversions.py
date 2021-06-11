#! /usr/bin/env python
"""
    O(nlogn) algorithm for Counting Inversions
    https://www.youtube.com/watch?v=I6ygiW8xN7Y&list=PLXFMmlk03Dt7Q0xr1PIAriY5623cKiH7V&index=15
"""


def sort_and_count_inversions(array):
    if len(array) < 2:
        return array, 0
    else:
        m = len(array) // 2
        larr, larr_inv = sort_and_count_inversions(array[:m])
        rarr, rarr_inv = sort_and_count_inversions(array[m:])
        combo_arr, split_inv = merge_and_compute_split(larr, rarr)
        return combo_arr, (larr_inv + rarr_inv + split_inv)


def merge_and_compute_split(larr, rarr):
    """
        This is a O(n) procedure => O(n) + O(n) actually
    :param larr: left split array
    :param rarr: right split array
    :return:
    """
    i, j, k = 0, 0, 0
    res_arr = []
    inversions = 0
    while i < len(larr) and j < len(rarr):
        if larr[i] < rarr[j]:
            res_arr.append(larr[i])
            i += 1
        elif larr[i] > rarr[j]:
            res_arr.append(rarr[j])
            j += 1
            inversions += (len(larr) - i)   # all remaining items in larr are GT current rarr element
        else:
            res_arr.append(larr[i])
            i += 1
            res_arr.append(rarr[j])
            j += 1
    res_arr.extend(larr[i:])
    res_arr.extend(rarr[j:])
    return res_arr, inversions


if __name__ == "__main__":
    arr = [1, 3, 5, 2, 4]
    print "Count of inversions = %d" % (sort_and_count_inversions(arr)[1])
