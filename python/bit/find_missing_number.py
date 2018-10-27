def find_missing_number(nums):
    sum_num = sum(nums)

    n = len(nums)
    total = n * (1 + n) // 2

    return total - sum_num


if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4, 5, 6, 8]
    assert find_missing_number(nums) == 7
