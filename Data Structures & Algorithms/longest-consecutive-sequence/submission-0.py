class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for num in nums:
            if num - 1 in seen:
                continue
            i = 1
            while num + i in seen:
                i += 1
            longest = max(longest, i)

        return longest