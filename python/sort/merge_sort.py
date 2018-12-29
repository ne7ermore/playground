def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right, arr.copy())


def merge(left, right, arr):
    l_index = r_index = 0
    while l_index < len(left) and r_index < len(right):
        if left[l_index] < right[r_index]:
            arr[l_index+r_index] = left[l_index]
            l_index += 1
        else:
            arr[l_index+r_index] = right[r_index]
            r_index += 1

    for i in range(l_index, len(left)):
        arr[i+r_index] = left[i]

    for i in range(r_index, len(right)):
        arr[l_index+i] = right[i]

    return arr


if __name__ == "__main__":
    arr = [10, 20, 5, 9, 3, 8, 12, 14, 90, 0, 60, 40, 23, 35, 95, 18]
    assert len(merge_sort(arr)) == len(arr)
    assert merge_sort(arr) == [0, 3, 5, 8, 9, 10, 12,
                               14, 18, 20, 23, 35, 40, 60, 90, 95]
