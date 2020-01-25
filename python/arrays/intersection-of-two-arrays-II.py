"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = collections.Counter(nums1)
        nums2 = collections.Counter(nums2)

        inter = nums1.keys() & nums2.keys()
        res = []
        for intt in inter:
            intt_count = min(nums1[intt], nums2[intt])
            res += [intt] * intt_count

        return res
