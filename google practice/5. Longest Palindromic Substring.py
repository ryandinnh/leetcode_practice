class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        top down dp approach, at each value of i check for longest even and odd palindrome with i as the center. 
        Return the longest value
        time complexity O(n^2)
        space complexity O(n)
        """
        #helper function to check for palindroms
        def subPalindrome(start, end):
            pal = ''
            palLength = 0
            while start >=0 and end < len(s) and s[start] == s[end]:
                if (end-start + 1) > palLength: #if current palindrom length is greater than max length
                    pal = s[start:end+1]
                    palLength = end-start + 1
                start -= 1
                end += 1
            
            return pal

        if len(s) <= 1:
            return s

        if len(s) == 2 and s[0] == s[1]:
            return s
        
        maxPal = ''
        #iterate over s try to find max palindrome
        for i in range(len(s)):
            #checking odd palindroms
            oddPal = subPalindrome(i, i)
            if len(oddPal) > len(maxPal):
                maxPal = oddPal

            #checking even
            evenPal = subPalindrome(i, i + 1)
            if len(evenPal) > len(maxPal):
                maxPal = evenPal
        
        return maxPal