def missing_ranges(arr, lo, hi):
    res, start = [], lo

    for n in arr:
        if n == start:
            start += 1
        elif n > start:
            res.append((start, n - 1))
            start = n + 1

    if start <= hi:
        res.append((start, hi))

    return res


if __name__ == "__main__":
    arr = [4, 9]
    lo = 1
    hi = 15

    res = missing_ranges(arr, lo, hi)

    assert len(res) == 3
    assert res[0] == (1, 3)
    assert res[1] == (5, 8)
    assert res[2] == (10, 15)
