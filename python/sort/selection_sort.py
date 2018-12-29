def selection_sort(arr):
    for i in range(len(arr)):
        cor_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[cor_index]:
                cor_index = j
        arr[i], arr[cor_index] = arr[cor_index], arr[i]

    return arr


if __name__ == "__main__":
    arr = [10, 20, 5, 9, 3, 8, 12, 14, 90, 0, 60, 40, 23, 35, 95, 18]
    assert len(selection_sort(arr)) == len(arr)
    assert selection_sort(arr) == [0, 3, 5, 8, 9, 10, 12,
                                   14, 18, 20, 23, 35, 40, 60, 90, 95]
