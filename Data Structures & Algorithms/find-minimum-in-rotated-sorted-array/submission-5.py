class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            n = nums[mid]
            print(l, mid, r)
            
            if mid > 0 and n < nums[mid - 1]:
                return n
            if mid == 0:
                if mid + 1 < len(nums):
                    return min(n, nums[mid + 1])
                return n
            
            if nums[l] > n:
                r = mid - 1
            elif n > nums[r]:
                l = mid + 1
            else:
                return nums[l]
