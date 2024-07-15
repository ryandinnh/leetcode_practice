class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        #first check for common divisor (1st base case)
        if str1 + str2 != str2 + str1:
            return ""
        #2nd base case
        elif str1 == str2: #so on further iterations if they ever equal it should return the GCD
            return str1
        #recursive cases (str1 or str2 greater):
        elif len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2) #str1[len(str2) this makes it so the new str1 has the prefix of str2 removed (start at index of length str2 till end)
        else: #condition where str2 is greater
            return self.gcdOfStrings(str1,str2[len(str1):])
        
#test case
solution = Solution()
str1 = "ABABAB"
str2 = "ABAB"
result = solution.gcdOfStrings(str1, str2)
print(result)  #output should be "AB"

"""
Runtime:
Base case 1 time: O(n+m) where n and m are the lengths of str1 and str2
base case 2:O(min(n,m)) because you just check the length of whichever is the shorter string

Recrusive time: O(log(min(n,m))) 

total runtime: O((n+m)⋅log(min(n,m)))
Recursive solutions use log as time as the problem size gets smaller every iteration
"""