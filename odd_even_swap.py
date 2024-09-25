"""
Given a positive integer n, you are allowed to swap any two adjacent digits if both digits are either even or odd. Your goal is to obtain the largest possible integer by performing a series of such swaps.

Constraints:
1 <= n <= 10^9
The integer n contains at least two digits.

Example:

Input: n = 597683
Output: 975863
Explanation:
Swap 5 and 9 -> 957683
Swap 5 and 7 -> 975683
Swap 6 and 8 -> 975863
No more swaps can be made to increase the number.

Input: n = 1234
Output: 1234
Explanation:
No more swaps can be made to increase the number.

Input: n = 2468
Output: 8642
Explanation:
Swap 2 and 4 -> 4268
Swap 4 and 6 -> 4628
Swap 6 and 8 -> 8642
No more swaps can be made to increase the number.

Input: n = 13579
Output: 97531
Explanation:
Swap 1 and 3 -> 31579
Swap 3 and 5 -> 51379
Swap 5 and 7 -> 71539
Swap 7 and 9 -> 97531
No more swaps can be made to increase the number.
"""
class Solution(): #first attempt is wrong because this only swaps ADJACENT digits
    def evenOddSwap(self, n: int) -> int:

        digits = list(str(n))

        for i in range(len(digits)-1):
            if (int(digits[i]) < int(digits[i+1])) and ((int(digits[i]) % 2 == 0 and int(digits[i+1]) % 2 == 0) or (int(digits[i]) % 2 != 0 and int(digits[i+1]) % 2 != 0)):
                digits[i], digits[i+1] = digits[i+1], digits[i] #swap the two index values
        
        return int("".join(digits))
    
class OptimizedSolution(): #pointers solution
    def evenOddSwap(self, n: int) -> int:
        digits = list(str(n))
        length = len(digits)
        i = 0 #index variable (start pointer)

        #iterate over the input integer
        while i < length - 1: #base case, end loop when index pointer reaches end of input integer
            j = i #second variable to represent an end pointer to determine how many adjacent elements with same parity (end pointer)

            #identify groups of adjacent digits with the same even/odd parity
            while j < length - 1 and int(digits[j]) % 2 == int(digits[j+1]) % 2: #ie. both adjacent elements are even
                j += 1 #this means that j will keep increasing from the initial starting index variable until the paritys are no longer the same

            if i != j:
                digits[i: j + 1] = sorted(digits[i: j + 1], reverse = True) #sort the selected group into descending 

            #i variable now moves on to the next index after the sorted group
            i = j+1
                 
        return int(''.join(digits))

    
sol = OptimizedSolution()

#Test cases
test_cases = [
    597683,  # Expected output: 975863
    1234,    # Expected output: 1234
    2468,    # Expected output: 8642
    13579,   # Expected output: 97531
    10203    # Expected output: 12003
]

# Run the test cases
for n in test_cases:
    result = sol.evenOddSwap(n)
    print(f"Input: {n}, Output: {result}")

#o(n) complexity for optimized solution