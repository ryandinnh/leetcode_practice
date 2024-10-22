from collections import Counter

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        sToT = {}
        tToS = {}
        
        for sChar, tChar in zip(s,t):
            if sChar in sToT and sToT[sChar] != tChar: 
                return False
            if tChar in tToS and tToS[tChar] != sChar:
                return False
            
            sToT[sChar] = tChar
            tToS[tChar] = sChar
    
        return True