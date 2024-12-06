class Solution(object):
    def houseRob(self, houses): #helper function with the search algo
            if len(houses) == 0:
                return 0
        
            if len(houses) == 1:
                return houses[0]

            prev1, prev2 = 0, 0
            for house in houses:
                current = max(prev1, prev2 + house)
                prev2, prev1 = prev1, current
            
            return prev1
            
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        difference between this and house robber 1 is that the input array is now circular
        run houserob1 search algo on nums[:-1] and nums [1:]
        return max value of above
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        firstCost = self.houseRob(nums[1:])
        lastCost = self.houseRob(nums[:-1])

        return max(firstCost, lastCost)