def insertion_sort(arr):
    for index in range(1, len(arr)):
        item = arr[index]
        for i in range(index):
            if item < arr[i]:
                arr.pop(index)
                arr.insert(i, item)
                break

    return arr


if __name__ == "__main__":
    arr = [10, 20, 5, 9, 3, 8, 12, 14, 90, 0, 60, 40, 23, 35, 95, 18]
    assert insertion_sort(arr) == [0, 3, 5, 8, 9,
                                   10, 12, 14, 18, 20, 23, 35, 40, 60, 90, 95]
