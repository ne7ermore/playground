def move_zeros(array):
    res, num = [], 0

    for i in range(len(array)):
        if array[i] is 0:  # avoid False by using 'is' not '=='
            num += 1
        else:
            res.append(array[i])

    return res + [0] * num


if __name__ == "__main__":
    assert move_zeros([False, 1, 0, 1, 2, 0, 1, 3, "a"]) == [
        False, 1, 1, 2, 1, 3, "a", 0, 0]
