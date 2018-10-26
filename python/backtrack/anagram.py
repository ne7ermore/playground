def anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    c1 = [0] * 26
    c2 = [0] * 26

    for s in s1:
        pos = ord(s) - ord("a")
        c1[pos] += 1

    for s in s2:
        pos = ord(s) - ord("a")
        c2[pos] += 1

    return c1 == c2


if __name__ == "__main__":
    s1 = "abcde"
    s2 = "bcdea"

    assert anagram(s1, s2)
