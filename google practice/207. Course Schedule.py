class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        """
        for a brute force approach you can build a hashmap as each pair is unique that basically is the rule for course completion
        - going through prequisites you add the first units in b, a order:
        - eg. prereq = [[0,1], [1, 2]]
        - first add:
            - 1, 0
        - second add:
        - 2, 1, 0

        if there is ever an add to the set where the units are already in it, check if b index is > than a index. if it is then keep iterating else you return false.
        if you can fully get through prereqs list then return true

        """
        preMap = {i: [] for i in range(numCourses)} #creates a dictionary of each course in numcourses with an empty list for prereqs
        for crs, pre in prerequisites: #populate courses with prereqs
            preMap[crs].append(pre) #use.append because it is a list as a value

        visited = set()
        def dfs(crs):
            #base cases
            if crs in visited: #loop case
                return False
            
            if preMap[crs] == []: #good base case because this is an end case
                return True
            
            visited.add(crs) #add this course to visited
            for pre in preMap[crs]: #run dfs on all of this courses prerequisites (next nodes)
                if not dfs(pre): #if any of them return false above then you can automatically break
                    return False

            visited.remove(crs) #remove from visit after traversing
            preMap[crs] = [] #if you cross over it again you can just return true so you dont need to do dfs on it again (saves complexity)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True