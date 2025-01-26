class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        right = n - 1
        maxArea = 0

        while left < right:
            area = min(height[left],height[right]) *(right - left)
            maxArea = max(maxArea, area)

            #b/c we are trying to maximize area, move the side which is lower 
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea