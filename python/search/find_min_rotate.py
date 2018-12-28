def find_min_rotate(array):
    high = len(array) - 1
    low = 0

    while low < high:
        mid = (high+low) // 2
        if array[mid] > array[high]:
            low = mid+1
        else:
            high = mid

    return array[low]


if __name__ == "__main__":
    array = [4, 5, 6, 7, 0, 1, 2]
    assert find_min_rotate(array) == 0
