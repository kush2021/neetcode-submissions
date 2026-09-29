class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {0: 0}

        def backtrack(i, left):
            if left in cache:
                return cache[left]
            if i < 0:
                return -1

            coin = coins[i]
            choose = -1
            if left - coin >= 0:
                choose = backtrack(i, left - coin)
            not_choose = backtrack(i - 1, left)
            
            if choose == -1:
                cache[left] = not_choose
                return not_choose
            if not_choose == -1:
                cache[left] = 1 + choose
                return 1 + choose
            cache[left] = min(1 + choose, not_choose)
            return min(1 + choose, not_choose)
        
        return backtrack(len(coins) - 1, amount)