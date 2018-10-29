def add_bitwise_operator(a, b):
    return (a ^ b) | ((a & b) << 1)


if __name__ == "__main__":
    assert add_bitwise_operator(3, 4) == 7
