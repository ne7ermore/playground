def rotate(arr, k):
    len_arr = len(arr)
    k %= len_arr
    return arr[len_arr - k:] + arr[:-k]


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print(rotate(arr, 12))
