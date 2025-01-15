class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) < 3: #in these combinations there is no way water can be trapped
            return 0 
        
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0,0
        water = 0

        while left <= right:
            if height[left] <= height[right]: #always compare the lower side
                #process left pointer
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    water += leftMax - height[left]
                left +=1
            else:
                #right pointer
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    water += rightMax - height[right]
                right -= 1

        
        return water