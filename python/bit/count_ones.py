def count_ones(n):
    count = 0
    while n:
        count += 1
        n &= n - 1

    return count


if __name__ == "__main__":
    assert count_ones(8) == 1
    assert count_ones(0) == 0
    assert count_ones(15) == 4
