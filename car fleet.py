class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Need to define rules for car fleet
        can combine the position and speed list as a tuple list to make it easier to iterate
            - use zip(list1, list2)
        sort the combined list by descending order, python will sort by first element in the tuple and then if there is a tie it will sort by second element
        now initialize a stack and iterate through combined list, adding the slopes for each car in the combined list
            - slope = (target - position) / speed
        while iterating just keep checking if the top slope of the stack is less than or equal to the second most top of the stack then pop the top value
            - ie. if the slope is faster than the top slope then the cars would be in the same fleet so you pop the top
        #space and time complexity o(n)
        """   
        slopes = []
        carPairs = [(p,s) for p, s in zip(position, speed)]
        carPairs.sort(reverse = True) #reverse sort to process cars from closest to target to farthest

        for p, s in carPairs:
            slopes.append((target-p) / s)
            if len(slopes) >= 2 and slopes[-1] <= slopes[-2]: #need the len(slopes) >= 2 so that the second condition can be checked
                slopes.pop()
        
        return len(slopes)
