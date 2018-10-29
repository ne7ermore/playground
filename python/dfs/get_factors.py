def get_factors(n):
    def factor(n, i, combi, res):
        while i * i <= n:
            if n % i == 0:
                res += combi + [i, int(n / i)],
                factor(n / i, i, combi + [i], res)
            i += 1
        return res
    return factor(n, 2, [], [])


if __name__ == "__main__":
    assert get_factors(16) == [[2, 8], [2, 2, 4], [2, 2, 2, 2], [4, 4]]
