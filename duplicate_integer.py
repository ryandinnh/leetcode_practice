class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for x in nums:
            for y in nums[nums.index(x)+1:]:
                if x == y:
                    return True
                else:
                    continue
        return False