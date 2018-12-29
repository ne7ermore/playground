def cycle_sort(arr):
    len_arr = len(arr)
    for cur in range(len_arr-1):
        item = arr[cur]
        index = cur

        for i in range(cur+1, len_arr):
            if item > arr[i]:
                index += 1

        arr[index], item = item, arr[index]

        while index != cur:
            index = cur
            for i in range(cur+1, len_arr):
                if item > arr[i]:
                    index += 1

            arr[index], item = item, arr[index]

    return arr


if __name__ == "__main__":
    arr = [10, 20, 5, 9, 3, 8, 12, 14, 90, 0, 60, 40, 23, 35, 95, 18]
    assert cycle_sort(arr) == [0, 3, 5, 8, 9, 10, 12,
                               14, 18, 20, 23, 35, 40, 60, 90, 95]
