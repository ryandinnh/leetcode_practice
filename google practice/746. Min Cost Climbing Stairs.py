class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        bottom up 1d DP approach
        Have cost itself be the array for DP
        append 0 at the end of DP as that is the cost of staying on the goal stair
        iterate backwards from the end index filling in the min cost of either going one step or two step towards the end
            - should be current index + min(index + 1 , index + 2)
        O(n) time and o(1) memory complexity b/c you modify directly into the input array
        """
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1): #need to do - 3 for the case that the array has less than 3 steps
            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0],cost[1])