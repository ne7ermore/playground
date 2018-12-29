def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    last = n
    while last > 1:
        for index in range(last-1):
            if arr[index] > arr[index+1]:
                swap(index, index+1)
        last -= 1

    return arr


if __name__ == "__main__":
    arr = [10, 20, 5, 9, 3, 8, 12, 14, 90, 0, 60, 40, 23, 35, 95, 18]
    assert bubble_sort(arr) == [0, 3, 5, 8, 9, 10,
                                12, 14, 18, 20, 23, 35, 40, 60, 90, 95]
