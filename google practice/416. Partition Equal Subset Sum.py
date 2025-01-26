class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2: #impossible to partition the subset if the sum is not divisible by 2 (even)
            return False

        dp = set() #dont need to include repeated targets
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) -1, -1, -1):
            nextDP = set() #nextDP is the remaining subarray
            #this will calculate all sums in the subset
            for t in dp:
                if (t+ nums[i]) == target: #optimzation is on iteration you check if adding the new num value to the existing targets == target then you find your subset
                    return True
                nextDP.add(t + nums[i]) # Add the new sum to the next set of possible sums
                nextDP.add(t) # Add the old sum (unchanged) to the next set of possible sums
            dp = nextDP

        return True if target in dp else False