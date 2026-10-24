class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count numbers
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        # frequency array
        freq = [[] for i in range(len(nums) + 1)]
        for key in count:
            freq[count[key]].append(key)
        # append to res
        res = []
        for i in range(len(freq) - 1, -1, -1):
            # remember that freq[i] is a list (can have multiple of same freq)
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res