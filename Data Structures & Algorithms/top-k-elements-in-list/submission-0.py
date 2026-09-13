class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        freq = [[] for _ in range(len(nums))]
        for n, c in count.items():
            freq[c - 1].append(n)

        i = 0
        j = len(nums) - 1
        top = []
        while i < k:
            for x in freq[j]:
                i += 1
                top.append(x)
            j -= 1

        return top