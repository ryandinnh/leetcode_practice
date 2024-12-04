class Solution(object):
    def rob(self, nums):
        """unoptimized
        
        :type nums: List[int]
        :rtype: int
        Time complexity: O(n^2) BECAUSE OF += MAX IN LOOP
        Space Complexity O(1)

        
        if len(nums) <= 2:
            return max(nums)
        if nums[-2] < nums[-1]:
            nums[-2] = nums[-1]
        for i in range(len(nums)-3, -1, -1): #can skip over last 2 index as its max cost are set before the loop
            nums[i] += max(nums[i+2:]) #it is not += nums[i+2] it should be the max value of the remaining values in dp except for nums+1
        
        return max(nums)
        """
        """
        optimized sOLUTION
        Time complexity: O(n)
        Space Complexity O(1)

        can optimize with pointers on the last two previous indexs
        this approach is a top down approach and i solved it iteratively
        """
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        prev1, prev2 = 0, 0 #prev2 tracks the maximum sum that excludes the current house and prev1 tracks the maximum sum that includes the current house.
        for num in nums:
            """
            Logic:
            For each house (represented by num), you decide whether to rob it or skip it:
            Rob it: Add num to prev2.
            Skip it: Use the value of prev1.
            Take the maximum of these two options for the current house.
            """
            current = max(prev1, prev2 + num) 
            prev2, prev1 = prev1, current
        
        return prev1



