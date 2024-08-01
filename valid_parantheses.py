class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if len(list(s)) % 2 != 0: #check if string is even (if odd then not valid)
            return False 
        for par in s:
            if par == '(': #for opening parantheses add close to stack to check at end
                stack.append(')')
            elif par == '[':
                stack.append(']')
            elif par == '{':
                stack.append('}')
            elif len(stack) != 0 and par == stack.pop(): #checking closing parantheses. If the stack is not empty and the correct closing parantheses is at the top of the stack(most recent add)
                continue #move onto next parantheses
            else: #fails check, ie. the correct closing parantheses is not at the top of the stack
                return False
        return True

#test    
solution = Solution()
print(solution.isValid('([{}])'))
print(solution.isValid('([)]'))