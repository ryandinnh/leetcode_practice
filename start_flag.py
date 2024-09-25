"""
You are given two integer arrays, arrayA and arrayB, both of the same length. You are also given a string startFlag which can be either "odd" or "even". Your task is to compute the sum of the differences between the elements of arrayA and arrayB for every odd or even index, depending on the value of startFlag.

If startFlag is "odd", calculate the sum of differences for all elements at odd indices (1, 3, 5, ...).
If startFlag is "even", calculate the sum of differences for all elements at even indices (0, 2, 4, ...).
The difference for each index i is calculated as arrayA[i] - arrayB[i].

If the total sum of these differences is greater than 0, return "A".
If the total sum is less than 0, return "B".
If the total sum is 0, return "Tie".

Example 1:
Input: 
arrayA = [5, 8, 7, 10, 12]
arrayB = [3, 6, 5, 9, 10]
startFlag = "even"

Output:
"A"

Example 2:
arrayA = [5, 8, 7, 10, 12]
arrayB = [3, 6, 5, 9, 10]
startFlag = "odd"

"Tie"

Example 3:
arrayA = [2, 4, 6, 8, 10]
arrayB = [3, 5, 7, 9, 11]
startFlag = "even"

"B"

Constraints:
1 <= len(arrayA), len(arrayB) <= 100
-100 <= arrayA[i], arrayB[i] <= 100
startFlag will be either "odd" or "even"
"""
class Solution: #first blind attempt
    def calculate_winner(self, arrayA: list[int], arrayB: list[int], startFlag: str) -> str:
        #helper function to calculate array diff
        def calc(a,b):
            return a - b
        
        sum = 0

        for i in range(len(arrayA)):
            if startFlag == "even":
                if i % 2 == 0: #even index
                    sum += calc(arrayA[i],arrayB[i])
                else:
                    continue
            else:
                if i % 2 != 0: #odd index
                    sum += calc(arrayA[i],arrayB[i])
                else:
                    continue
        #winning conditions
        if sum > 0:
            return "A"
        elif sum == 0:
            return "Tie"
        else:
            return "B"
        
class OptimizedSolution(): #same run time but better code clarity
    def calculate_winner(self, arrayA: list[int], arrayB: list[int], startFlag: str) -> str:
        sum = 0
        """
        start = 0
        if startFlag == 'Even':
            start = 0
        if startFlag == 'Odd':
            start = 1
        """
        #better way to do above:
        start = 0 if startFlag == 'even' else 1

        for i in range(start,len(arrayA),2):
            sum += arrayA[i] - arrayB[i]
        
        if sum > 0:
            return "A"
        elif sum == 0:
            return "Tie"
        else:
            return "B"

#test cases:
#solution = Solution()
solution = OptimizedSolution()
test_cases = [
    ([5, 8, 7, 10, 12], [3, 6, 5, 9, 10], "even", "A"),  # Example 1
    ([5, 8, 7, 10, 12], [3, 6, 5, 9, 10], "odd", "A"),   # Example 2
    ([2, 4, 6, 8, 10], [3, 5, 7, 9, 11], "even", "B"),    # Example 3
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], "even", "Tie")    # Additional tie case
]

#Running test cases
for i, (arrayA, arrayB, startFlag, expected) in enumerate(test_cases):
    result = solution.calculate_winner(arrayA, arrayB, startFlag)
    print(f"Test Case {i + 1}:")
    print(f"Input: arrayA = {arrayA}, arrayB = {arrayB}, startFlag = '{startFlag}'")
    print(f"Expected Output: {expected}")
    print(f"Actual Output: {result}")
    print(f"Test Result: {'PASS' if result == expected else 'FAIL'}\n")       