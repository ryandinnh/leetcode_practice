class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 4:
            return 0
        else:
            temp = sorted(nums[:])
            minDiff = float("inf")

            #3 changes so there are 4 cases
            minDiff = min(
                temp[-4] - temp[0], #3 largest removed
                temp[-3] - temp[1], #2 largest removed and lowest removed
                temp[-2] - temp[2], #largest removed and 2 lowest removed
                temp[-1] - temp[3] #3 lowest removed
            )

            return minDiff
        