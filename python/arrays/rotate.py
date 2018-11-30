def rotate(arr, k):
    len_arr = len(arr)
    k %= len_arr
    return arr[len_arr - k:] + arr[:-k]


if __name__ == "__main__":
    assert rotate([1, 2, 3, 4, 5, 6, 7, 8], 4) == [5, 6, 7, 8, 1, 2, 3, 4]
