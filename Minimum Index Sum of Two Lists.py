class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        commonStrings = {} # string : index sum
        #iterate over list1 using index
        for i in range(len(list1)):
            if list1[i] in list2:
        #find index of both strings and add them
                iSum = i + list2.index(list1[i])
        
        #add string and index sum to a dictionary
                commonStrings[list1[i]] = iSum
            
        #return the lowest value in the dictionary
        minValue = min(commonStrings.values())
        return [key for key, value in commonStrings.items() if value == minValue]