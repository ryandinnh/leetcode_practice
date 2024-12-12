class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        time-complexity O(n^2)
        """
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1): #default end value is 1
            for j in range(i + 1, len(nums)): #because you can skip values in the subsequence you need to check all remaining
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)