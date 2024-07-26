class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0 #represents how many flowers planted
        
        #for loop representing index of flowerbed
        for i in range(len(flowerbed)): #remember this solution
            #seeing if pot can be planted
            #(i == 0 or flowerbed[i-1] == 0) determines if you are on the first index and if you are then you do not need to check the preceding pot (bc you cant)
            #same idea for the third boolean but with the last value
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1 #allows you to update flowerbed without using it as a loop
                count += 1
                if count >= n:
                    return True
        
        return count >= n #if count is less than n then there is not enough pots left to place
    
#test cases
flowerbed = [1, 0, 0, 0, 1]
n = 1
print(Solution().canPlaceFlowers(flowerbed, n))  #Output: True

flowerbed = [1, 0, 0, 0, 1]
n = 2
print(Solution().canPlaceFlowers(flowerbed, n))  #Output: False