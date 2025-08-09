class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low, high = 1, max(piles) #set range for binary search
        while low < high:
            mid = (high + low) // 2
            hoursNeeded = sum((pile + mid - 1) // mid for pile in piles)

            if hoursNeeded > h:
                low = mid + 1 #since low is getting the plus 1 it will defualt for the answer
            else:
                high = mid
        
        return low