class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        time complexity O(N)
        space: O(N)
        """
        stack = []
        maxA = 0
        n = len(heights)

        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                top = stack.pop()
                height = heights[top] #max height in the stack
                width = i - stack[-1] - 1 if stack else i #left - righht - 1
                maxA = max(maxA, height * width)
            stack.append(i) #push current index into the stack to check

        while stack: #for max output still need to calculate values in the stack
            top = stack.pop()
            height = heights[top]
            width  = n - stack[-1] - 1 if stack else n
            maxA = max(maxA, width * height)

        return maxA