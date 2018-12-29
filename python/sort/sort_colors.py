def sort_colors(arr):
    n = len(arr)
    index = n-1
    res_arr, sums = [1]*n, 0

    for v in arr:
        if v == 2:
            res_arr[index] = v
            index -= 1

        else:
            sums += v

    zero_nums = index+1-sums
    zeros = [0]*(zero_nums)
    zeros.extend(res_arr[zero_nums:])

    return zeros


if __name__ == "__main__":
    arr = [0, 1, 1, 1, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 2, 2]
    assert len(sort_colors(arr)) == len(arr)
    assert sort_colors(arr) == [0, 0, 0, 0, 0, 0, 0,
                                1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
