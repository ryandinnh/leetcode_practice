class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        output = []
        maxVal = max(candies)

        for candy in candies:
            if candy + extraCandies >= maxVal:
                output.append(True)
            else:
                output.append(False)

        return output
                