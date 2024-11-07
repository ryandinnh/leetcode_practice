"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        A deep copy is essentially a clone of the input graph
        use a hashmap and DFS/BFS to solve

        Use a hashmap to map the old nodes to the new nodes
        
        recursive part is looking at node neighbors that you need to clone
        if the neighbor your looking to clone is already in the hashmap then you can initialize that there is an edge between those two nodes
        ie. they are neighbors

        time complexity = O(n) where n = edges + vertices
        """
        nodeMap = {} #old : new

        def dfs(node):
            if node in nodeMap: #if the node we're looking at is already mapped then we just return the clone
                return nodeMap[node]
            
            #if not mapped create a copy with the original nodes value and map it in the hash map
            copy = Node(node.val)
            nodeMap[node] = copy

            #next we want to copy each neighboring node of the current node and add it the copy nodes neighboring values
            for neighbor in node.neighbors: #from the constructor class can see neighbors is a list
                copy.neighbors.append(dfs(neighbor)) 
            
            return copy
        
        # did not check for empty list edge case
        return dfs(node) if node else None
