def heap_sort(arr):
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def heapfy(arr, index, end):
        len_arr = len(arr[:end])
        while index*2+1 < len_arr:
            child = index*2 + 1

            if child+1 < len_arr and arr[child] < arr[child+1]:
                child += 1

            if arr[index] > arr[child]:
                break

            swap(arr, index, child)

            index = child

    len_arr = len(arr)
    for i in range(len_arr//2, -1, -1):
        heapfy(arr, i, len_arr-1)

    for i in range(len_arr-1, 0, -1):
        swap(arr, 0, i)
        heapfy(arr, 0, i)

    return arr


if __name__ == "__main__":
    arr = [10, 20, 5, 9, 3, 8, 12, 14, 90, 0, 60, 40, 23, 35, 95, 18]
    assert heap_sort(arr) == [0, 3, 5, 8, 9, 10, 12,
                              14, 18, 20, 23, 35, 40, 60, 90, 95]
