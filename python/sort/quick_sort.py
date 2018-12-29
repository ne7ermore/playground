def quick_sort(arr):
    def partition(arr, left, right):
        store_index = left
        for i in range(left, right):
            if arr[i] < arr[right]:
                arr[i], arr[store_index] = arr[store_index], arr[i]
                store_index += 1

        arr[right], arr[store_index] = arr[store_index], arr[right]

        return store_index

    def quick_sort_recur(arr, left, right):
        if left < right:
            store_index = partition(arr, left, right)

            quick_sort_recur(arr, left, store_index-1)
            quick_sort_recur(arr, store_index+1, right)

    quick_sort_recur(arr, 0, len(arr)-1)

    return arr


if __name__ == "__main__":
    arr = [10, 20, 5, 9, 3, 8, 12, 14, 90, 0, 60, 40, 23, 35, 95, 18]
    assert len(quick_sort(arr)) == len(arr)
    assert quick_sort(arr) == [0, 3, 5, 8, 9, 10, 12,
                               14, 18, 20, 23, 35, 40, 60, 90, 95]
