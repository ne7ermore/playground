def word_range(word):
    for ind in range(len(word)):
        temp = word[ind]
        for c in [chr(x) for x in range(ord('a'), ord('z') + 1)]:
            if c != temp:
                yield word[:ind] + c + word[ind + 1:]


def ladder_length(begin_word, end_word, word_list):
    if len(begin_word) != len(end_word):
        return -1

    if begin_word == end_word:
        return 0

    if sum(c1 != c2 for c1, c2 in zip(begin_word, end_word)) == 1:
        return 1

    begin_set = set()
    end_set = set()
    begin_set.add(begin_word)
    end_set.add(end_word)
    result = 2
    while begin_set and end_set:

        if len(begin_set) > len(end_set):
            begin_set, end_set = end_set, begin_set

        next_begin_set = set()
        for word in begin_set:
            for ladder_word in word_range(word):
                if ladder_word in end_set:
                    return result
                if ladder_word in word_list:
                    next_begin_set.add(ladder_word)
                    word_list.remove(ladder_word)
        begin_set = next_begin_set
        result += 1

    return -1


if __name__ == "__main__":
    assert ladder_length(
        'hit', 'cog', ["hot", "dot", "dog", "lot", "log"]) == 5
