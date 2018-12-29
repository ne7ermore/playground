def bitonic_sort(arr, reverse):
    def compare(arr, reverse):
        n = len(arr) // 2
        for i in range(n):
            if reverse != (arr[i] > arr[i+n]):
                arr[i], arr[i+n] = arr[i+n], arr[i]

        return arr

    def bitonic_merge(arr, reverse):
        n = len(arr)

        if n <= 1:
            return arr

        arr = compare(arr, reverse)
        left = bitonic_merge(arr[:n // 2], reverse)
        right = bitonic_merge(arr[n // 2:], reverse)
        return left + right

    n = len(arr)

    if n <= 1:
        return arr

    assert n & n-1 == 0

    left = bitonic_sort(arr[:n // 2], True)
    right = bitonic_sort(arr[n // 2:], False)

    arr = bitonic_merge(left + right, reverse)

    return arr


if __name__ == "__main__":
    arr = [10, 20, 5, 9, 3, 8, 12, 14, 90, 0, 60, 40, 23, 35, 95, 18]

    assert bitonic_sort(arr, False) == [
        0, 3, 5, 8, 9, 10, 12, 14, 18, 20, 23, 35, 40, 60, 90, 95]
