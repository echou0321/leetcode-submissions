class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for num, count in count.items():
            freq[count].append(num)
        
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                if k == 0:
                    return res
                res.append(num)
                k -= 1
        return res