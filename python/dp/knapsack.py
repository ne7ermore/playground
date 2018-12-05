class Item(object):
    def __init__(self, weight, value):
        self.v = value
        self.w = weight


def max_value(items, knapsack):
    dp = [[0] * len(items) for _ in range(knapsack + 1)]
    for c in range(1, knapsack + 1):
        if items[0].w <= c:
            dp[c][0] = items[0].v

        for index in range(1, len(items)):
            if items[index].w <= c:
                dp[c][index] = max(
                    items[index].v + dp[c - items[index].w][index - 1], dp[c][index - 1])
            else:
                dp[c][index] = dp[c][index - 1]
    return dp[-1][-1]


if __name__ == "__main__":
    items = [Item(5, 12), Item(4, 3), Item(7, 10), Item(2, 3), Item(6, 6)]
    assert max_value(items, 15) == 25
