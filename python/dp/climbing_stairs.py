def climb_stairs(n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    assert climb_stairs_optimized(4) == 5
