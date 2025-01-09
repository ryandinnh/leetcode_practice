class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Time complexity O(N^2)
        """
        nums.sort() #sort the input array into ascending order
        output = []
        for i in range(len(nums)):
            #skip dupes
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i+1
            right = len(nums)-1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates for `left` and `right`
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
            
        
        return output
