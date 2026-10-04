class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = nums[0]
        maxProd = nums[0]
        minProd = nums[0]

        for i in range(1, len(nums)):
            tmp = maxProd
            maxProd = max(nums[i] * maxProd, nums[i] * minProd, nums[i])
            minProd = min(nums[i] * tmp, nums[i] * minProd, nums[i])
            best = max(maxProd, best)

        return best