class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []

        def backtrack(cur: List[int], target: int, i: int):
            if target < 0:
                return
            if target == 0:
                nonlocal ans
                ans.append(cur.copy())
                return
            
            for j in range(i, len(nums)):
                cur.append(nums[j])
                backtrack(cur, target - nums[j], j)
                cur.pop()

        backtrack([], target, 0)
        return ans