class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        sortedNums = sorted(set(nums)) #use set to remove duplicates

        length = 1
        temp = 1

        for i in range(1,len(sortedNums)):
            if sortedNums[i] == sortedNums[i-1] + 1:
                temp += 1
            else:
                length = max(temp,length)
                temp = 1
        
        length = max(temp,length) #need a last check if the length ends at the last index
        return length