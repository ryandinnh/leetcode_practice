class Solution(object):
    def maxProduct(self, nums):
        """
        brute force? O(n^2)
        - try every single sub array combination   
        aka kadane's algorithm
        """
        #set default to max value in nums because 0 doesnt work when the input array is all negative or something like [-1]
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            temp = curMax #need tthis line bc in curMax calc u modify it already
            #these represent the decions you can take in the tree, multipy by max previous subarray, multipy by min subarray, or start new subarray
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(n * temp, n * curMin, n)
            res = max(res, curMax)
        
        return res