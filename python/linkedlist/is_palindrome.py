def is_palindrome_dict(list):
    if len(list) < 2:
        return True

    d = {}
    for index, num in enumerate(list):
        if num in d:
            d[num].append(index)
        else:
            d[num] = [index]

    checksum = index
    middle = 0
    for v in d.values():
        if len(v) % 2 != 0:
            middle += 1

        else:
            for index in range(len(v) // 2):
                if v[index] + v[len(v) - 1 - index] != checksum:
                    return False

        if middle > 1:
            return False

    return True


if __name__ == "__main__":
    list = [1, 1, 2, 3, 2, 1, 1]
    assert is_palindrome_dict(list)
