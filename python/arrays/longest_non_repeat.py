def longest_non_repeat(string):
    start = 0
    used_char, temp = {}, ""

    for index, char in enumerate(string):
        if char in used_char and start <= used_char[char]:
            if len(temp) < index - start + 1:
                temp = string[start:index]
            start = used_char[char] + 1

        used_char[char] = index
    return temp


if __name__ == "__main__":
    s = "abcabcdddabcdftghooooabcdftghoo"
    subs = longest_non_repeat(s)
    assert subs == "abcdftgho"
