def generate_abbreviations(word):

    def backtrack(result, word, pos, count, cur):
        if pos == len(word):
            if count > 0:
                cur += str(count)
            result.append(cur)
            return

        if count > 0:
            backtrack(result, word, pos + 1, 0, cur + str(count) + word[pos])
        else:
            backtrack(result, word, pos + 1, 0, cur + word[pos])

        backtrack(result, word, pos + 1, count + 1, cur)

    result = []
    backtrack(result, word, 0, 0, "")
    return result


if __name__ == "__main__":
    res = generate_abbreviations("abc")
    print(res)
