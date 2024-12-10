class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        im thinking bottom up dp approach you just keep adding how many combos u can get based on the previous decoding
        """
        dp = {len(s) : 1}
        def dfs(i):
            if i in dp: #base case
                return dp[i]
            if s[i] == "0": #base case
                return 0
            
            #encoding 1 digit
            res = dfs(i + 1)

            #encoding 2 digits
            #check if i is in range of the string, if i starts with 1 then the second digit can be any value 0-9
            #if i starts with 2 you can only take 2 digits when i + 1 is between 0-6 as the alphabet ends at 26
            if (i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i+1] in '0123456')):
                res += dfs(i + 2)
                
            dp[i] = res
            return res
        
        return dfs(0)

   

        