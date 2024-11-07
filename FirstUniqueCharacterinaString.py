from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #create a dictionary where its char : frequency
        charFreq = Counter(s)
        
        #return the first key where its value equals 1'
        for i, char  in enumerate(s):
            if charFreq[char] == 1:
                return i
        
        #return -1 if thats none in the dictionary
        
        return -1