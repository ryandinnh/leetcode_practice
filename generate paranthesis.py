class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #have variables for open and close paranthesis

        #so if n = 3 you know you want every combination of o = 3 and c = 3
        #only add an open paranthesis if o < n
        #only add a closing paranthesis if c < o
        #valid if o = c = n
        stack = []
        res = []

        def backtrack(o, c):
            if o == c == n:
                res.append("".join(stack))
                return
            
            if o < n:
                stack.append('(')
                backtrack(o + 1, c) #recursively call backtrack
                stack.pop()
            
            if c < o:
                stack.append(")")
                backtrack(o, c + 1)
                stack.pop()

        backtrack(0,0)    
        return res