from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        out = []
        
        # create a dictionary for both list where int : frequency
        dict1 = dict(Counter(nums1))
        dict2 = dict(Counter(nums2))
        
        
        # iterate over one dictionary seeing if that key value also appears in the second dictionary
        for num1 in dict1.keys():
            if num1 in dict2:
                count1 = dict1[num1]
                count2 = dict2[num1]
                while count1 > 0 and count2 > 0:
                    out.append(num1)
                    count1 -= 1
                    count2 -= 1
        # if yes then add that key value to an output list and subtract the value for that key by 1 for both dictionaries
        # keep adding until a value equals 0 
        
        #return output list
        return out