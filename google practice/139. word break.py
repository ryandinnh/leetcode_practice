class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1) #need +1 for basecase
        dp[len(s)] = True #out of bound position is base case

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w: #need to check if i has even enough characters to compare with w
                    dp[i] = dp[i+ len(w)]
                if dp[i]:
                    break

        return dp[0]