def longest_non_repeat(string):
    start = max_len = 0
    used_char = {}

    for index, char in enumerate(string):
        if char in used_char and start <= used_char[char]:
            # dup char, refresh start
            start = used_char[char] + 1
            subs = []
        else:
            max_len = max(max_len, index - start + 1)

        used_char[char] = index
    return max_len, string[start:start + max_len]


if __name__ == "__main__":
    s = "abcabcdftghddabcdftgho"
    ml, subs = longest_non_repeat(s)
    assert ml == 9
    assert subs == "abcdftgho"
