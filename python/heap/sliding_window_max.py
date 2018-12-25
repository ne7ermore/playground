def max_sliding_window(nums, k):
    return [max(nums[index - k:index]) for index in range(k, len(nums) + 1)]


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    assert max_sliding_window(nums, k) == [3, 3, 5, 5, 6, 7]
