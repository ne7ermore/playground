def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pos = arr[0]
    less = [n for n in arr[1:] if n <= pos]
    greater = [n for n in arr[1:] if n > pos]

    return quick_sort(less) + [pos] + quick_sort(greater)


if __name__ == "__main__":
    arr = [10, 20, 5, 9, 3, 8, 12, 14, 90, 0, 60, 40, 23, 35, 95, 18]
    assert len(quick_sort(arr)) == len(arr)
    assert quick_sort(arr) == [0, 3, 5, 8, 9, 10, 12,
                               14, 18, 20, 23, 35, 40, 60, 90, 95]
