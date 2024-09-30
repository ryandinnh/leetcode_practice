class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {} #integer val : frequency

        integers = set(nums)

        for integer in integers:
            frequencies[integer] = nums.count(integer)

        output = []

        while k > 0:
            maxKey = max(frequencies, key=frequencies.get)
            output.append(maxKey)
            frequencies.pop(maxKey)
            k-=1

        return output