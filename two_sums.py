#needed help on this
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {} #value : index
        for index, value in enumerate(nums): #enumerate nums makes it so the list is seperated by index, value
            find = target - value #note find is a VALUE
            if find in nums_dict: #if the difference between target and value is in the dictionary then return both indexs
                return [nums_dict[find], index]
            nums_dict[value] = index #if the difference cant be found then update the dictionary with that index and value and continue to iterate over nums
            
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(solution.twoSum([3, 2, 4], 6))  # Output: [1, 2]
print(solution.twoSum([3, 3], 6))     # Output: [0, 1]           

#time complexity:
"""
The solution is O(n) - worst case the the time-complexity is n
This is because the code only iterates through the list nums once making it so in the worst case where the solutions are the last two indexs, the code will only run n times where n is the length of the list.
This is possible as the python function enumerate is used to split the list instead of having to create a new dictionary with items value : index. 
"""