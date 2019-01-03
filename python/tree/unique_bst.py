def unique_bst(n):
    assert n >= 0
    if n < 2:
        return 1

    dp = [0]*(n+1)
    dp[1], dp[0] = 1, 1

    for i in range(2, n+1):
        for j in range(i):
            dp[i] += dp[j]*dp[i-1-j]

    return dp[-1]


if __name__ == "__main__":
    assert unique_bst(3) == 5
