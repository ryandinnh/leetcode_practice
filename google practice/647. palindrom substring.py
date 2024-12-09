class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        thinking of iterating over input array s with helper function palCount
            - palCount will use s[i-1] and s[i+1] as start and end pointers iterate through the entire array checking for palindroms and return a count of how many palindromes there are with s[i] as a center point/
            - remember to default add 1 to the helper function as s[i] itself is a palindrom
            - check for even and odd palindroms
        time complexity O(n^2)
        space complexity O(1)
        """
        #two pointer method to check for substrings
        def palCount(start, end):
            subCount = 0
            while start >=0 and end < len(s) and s[start] == s[end]:
                subCount += 1
                start -= 1
                end += 1
            
            return subCount
        
        count = 0
        for i in range(len(s)):
            count +=1 #s[i] itself is already a palindrom
            count += palCount(i-1, i+1) #odd palindroms
            count += palCount(i,i+1) #even palindroms
        
        return count


        