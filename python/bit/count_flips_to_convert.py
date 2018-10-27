def count_flips_to_convert(a, b):

    diff = a ^ b

    count = 0
    while diff:
        diff &= (diff - 1)
        count += 1
    return count


if __name__ == "__main__":
    assert count_flips_to_convert(15, 29) == 2
