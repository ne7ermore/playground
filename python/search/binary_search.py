def binary_search(list, num):
    high = len(list)
    low = 0
    mid = (high+low) // 2

    while True:
        mid = (high+low) // 2
        if num > list[mid]:
            low = mid + 1
        elif num < list[mid]:
            high = mid
        else:
            return mid


if __name__ == "__main__":
    l = [2, 4, 6, 7, 8, 9, 11, 15, 18, 21, 31, 64]
    assert binary_search(l, 18) == 8
