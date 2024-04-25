#!/usr/bin/env python3

def find_peak(list_of_integers):
    arr = list_of_integers
    if not arr:
        return None

    def peak(arr, start, stop, depth=0, max_depth=1000):
        if depth > max_depth:
            raise RecursionError("Max depth exceeded")

        mid = (stop + start) // 2
        if start >= stop or mid == 0:
            return arr[mid]

        if (arr[mid] > arr[mid - 1]):
            if (arr[mid] > arr[mid + 1]):
                return arr[mid]
            return peak(arr, mid, stop, depth+1, max_depth)
        elif (arr[mid] < arr[mid - 1]):
            if (arr[mid] > arr[mid + 1]):
                return peak(arr, start, mid, depth+1, max_depth)
            return peak(arr, start, mid - 1, depth+1, max_depth)
        else:
            peak_left = peak(arr, start, mid - 1, depth+1, max_depth)
            peak_right = peak(arr, mid + 1, stop, depth+1, max_depth)
            return max(peak_left, peak_right)

    return peak(arr, 0, len(arr) - 1)
