def summarize_ranges(arr):
    rec = [arr[i] - arr[i - 1] for i in range(1, len(arr))]
    idx = [index for index, x in enumerate(rec) if x != 1]

    res, start = [], 0
    for x in idx:
        res.append((arr[start], arr[x]))
        start = x + 1
    res.append((arr[start], arr[-1]))

    return res


if __name__ == "__main__":
    arr = [0, 1, 2, 4, 5, 7, 8, 9, 10, 11, 20, 21]

    res = summarize_ranges(arr)

    assert res[0] == (0, 2)
    assert res[1] == (4, 5)
    assert res[2] == (7, 11)
    assert res[3] == (20, 21)
