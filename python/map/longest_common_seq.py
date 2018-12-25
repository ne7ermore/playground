def longest_common_seq(s1, s2):
    len1, len2 = len(s1), len(s2)

    res = [[0]*(len2+1) for _ in range((len1+1))]

    for j in range(1, len2+1):
        for i in range(1, len1+1):
            if s1[i-1] == s2[j-1]:
                res[i][j] = res[i-1][j-1] + 1
            else:
                res[i][j] = max(res[i-1][j], res[i][j-1])

    out = []
    while len1 > 0 and len2 > 0:
        if s1[len1-1] == s2[len2-1]:
            out.append(s1[len1-1])
            len1 -= 1
            len2 -= 1
        elif res[len1-1][len2] == res[len1][len2-1]:
            len2 -= 1
        elif res[len1-1][len2] > res[len1][len2-1]:
            len1 -= 1
        else:
            len2 -= 1

    out.reverse()
    return out


if __name__ == "__main__":
    s1 = "13456778"
    s2 = "357486782"

    assert longest_common_seq(s1, s2) == ['3', '5', '7', '7', '8']
