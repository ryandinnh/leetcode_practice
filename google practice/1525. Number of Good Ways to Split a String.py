class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        leftCounts = [0] * len(s)
        rightCounts = [0]* len(s)

        leftSeen = set()
        rightSeen = set()

        for i in range(len(s)):
            leftSeen.add(s[i])
            leftCounts[i] = len(leftSeen) #append on how many unique units from begining to index i

        for i in range(len(s) - 1, -1, -1): #going in reverse
           rightSeen.add(s[i])
           rightCounts[i] = len(rightSeen)

        splits = 0
        for i in range(len(s) - 1):
            if leftCounts[i] == rightCounts[i+1]:
                splits +=1
        
        return splits
        