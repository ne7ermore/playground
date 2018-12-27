from copy import deepcopy


def rotate90(m):
    el_len = len(m[0])
    new_m = [[0]*len(m) for _ in range(el_len)]
    for i, row in enumerate(m):
        for j, elem in enumerate(row):
            new_m[el_len-1-j][i] = elem

    return new_m


def rotate180(m):
    for row in m:
        row = row.reverse()

    return m


def rotate270(m):
    new_m = [[0]*len(m) for _ in range(len(m[0]))]
    for i, row in enumerate(m):
        for j, elem in enumerate(row):
            new_m[j][i] = elem

    return new_m


if __name__ == "__main__":
    m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

    m1 = deepcopy(m)
    assert rotate90(m1) == [[4, 8, 12], [3, 7, 11], [2, 6, 10], [1, 5, 9]]

    m1 = deepcopy(m)
    assert rotate180(m1) == [[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9]]

    m1 = deepcopy(m)
    assert rotate270(m1) == [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
