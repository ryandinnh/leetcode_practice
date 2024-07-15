#my original solution
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        output = ""
        tuple1 = tuple(word1)
        tuple2 = tuple(word2)

        if len(word1) == len(word2):
            for x in range(len(word2)):
                output += tuple1[x]
                output += tuple2[x]

        if len(word1) > len(word2):
            for x in range(len(word2)):
                output += tuple1[x]
                output += tuple2[x]
            for y in range(len(word2), len(word1)):  # fixed the range to len(word1) instead of len(word1) + 1
                output += tuple1[y]
        
        if len(word1) < len(word2):
            for x in range(len(word1)):
                output += tuple1[x]
                output += tuple2[x]
            for y in range(len(word1), len(word2)):
                output += tuple2[y]
        
        return output

#optimized solution:
class OptimizedSolution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        output = [] #no tuple initialization required, can solve with two pointers and a list to collect characters.
        i, j = 0, 0
        len1, len2 = len(word1), len(word2) #early initialization so dont need to keep calling for len()

        while i < len1 and j < len2: #initial loop to append characters to the output list until one of the pointers reaches the end of either word
            output.append(word1[i])
            output.append(word2[j])
            i += 1 #update the pointers with the next index position
            j += 1

        #Second loop to append the remaining part of the longer word
        if i < len1:
            output.append(word1[i:])
        if j < len2:
            output.append(word2[j:])

        return ''.join(output) #.join() puts togethor all characters in the list as a single string. The '' determines the positions to join (all of them)

solution = Solution()
#solution = OptimizedSolution()

"""
Time cases:
My original solution was O((n+m)^2) due to the repeated string concatenations 
Optimized solution: O(n+m)

where n and m are the lengths of word1 and word2.
"""

#test cases:
# Example 1
word1 = "abc"
word2 = "pqr"
print(solution.mergeAlternately(word1, word2))  # Output: "apbqcr"

# Example 2
word1 = "ab"
word2 = "pqrs"
print(solution.mergeAlternately(word1, word2))  # Output: "apbqrs"

# Example 3
word1 = "abcd"
word2 = "pq"
print(solution.mergeAlternately(word1, word2))  # Output: "apbqcd"
