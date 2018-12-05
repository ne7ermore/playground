def robber(houses):
    last, now = 0, 0
    for h in houses:
        tmp = now
        now = max(now, last + h)
        last = tmp
        print(last, now, h)

    return now


if __name__ == "__main__":
    houses = [1, 2, 16, 3, 1, 15, 3, 12, 1]
    assert robber(houses) == 44
