#!/usr/bin/env python3

def find_peak(list_of_integers):
    arr = list_of_integers
    if not arr:
        return None

    def peak(arr, start, stop):
        mid = (stop + start) // 2
        if start >= stop or mid == 0:
            print("base case hit :")
            print(arr[start: stop + 1])
            return arr[mid]
        print(start, mid, stop)

        if (arr[mid] > arr[mid - 1]):
            print("case 1")
            if (arr[mid] > arr[mid + 1]):
                return arr[mid]
            return peak(arr, mid, stop)
        elif (arr[mid] < arr[mid - 1]):
            print("case 2")
            if (arr[mid] > arr[mid + 1]):
                return peak(arr, start, mid)
            return peak(arr, start, mid - 1)
        else:
            print("case 3")
            peak_left = peak(arr, start, mid - 1)
            peak_right = peak(arr, mid + 1, stop)
            return max(peak_left, peak_right)

    print(peak(arr, 0, len(arr) - 1))


# find_peak([1, 0, 3, 2])
