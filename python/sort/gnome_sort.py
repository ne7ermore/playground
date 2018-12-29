def gnome_sort(arr):
    len_arr = len(arr)
    index = 0

    while index < len_arr:
        if index == 0 or arr[index-1] < arr[index]:
            index += 1
        else:
            arr[index-1], arr[index] = arr[index], arr[index-1]
            index -= 1

    return arr


if __name__ == "__main__":
    arr = [10, 20, 5, 9, 3, 8, 12, 14, 90, 0, 60, 40, 23, 35, 95, 18]
    assert gnome_sort(arr) == [0, 3, 5, 8, 9, 10, 12,
                               14, 18, 20, 23, 35, 40, 60, 90, 95]
