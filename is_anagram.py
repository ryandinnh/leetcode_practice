class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #both strings have to have the same length to be anagrams
            return False
        
        #hash maps to count letter frequencies
        countS = {}
        countT = {}

        #populate the hashmaps:
        for char in s: #python allows you to iterate over strings by default it goes character by character
            #key is the character and value is the count
            #hashMap.get(key, default) is used to get the value of a key element in the dictionary. If there is no value associated with the key, the default arg is used to initialize the value. In this case it would be 0 as we are adding 1 to it already to update it.
            countS[char] = countS.get(char, 0) + 1 

        for char in t:
            countT[char] = countT.get(char, 0) + 1

        #compare two dictionares with a conditional statement
        return countS == countT
    
#this solution is now in O(m+n) time as we only iterate through each list once
solution = Solution()

#Test cases
test_cases = [
    ("anagram", "nagaram"),  # Expected output: True
    ("rat", "car"),          # Expected output: False
    ("hello", "lleho"),      # Expected output: True
    ("aabbcc", "abcabc"),    # Expected output: True
    ("test", "ttew"),        # Expected output: False
    ("", ""),                # Expected output: True (both are empty strings)
]

for s, t in test_cases:
    result = solution.isAnagram(s, t)
    print(f"\nisAnagram('{s}', '{t}') = {result}")
