class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '/', '*']

        for x in tokens:
            if x in ops:
                m = stack.pop()
                n = stack.pop()

                if x == '+':
                    stack.append(m + n)
                elif x == '-':
                    stack.append(n - m)
                elif x == '/':
                    stack.append(int(n / m)) #need int here so that division between integers always truncates toward zero.
                elif x == '*':
                    stack.append(m * n)
            else:
                stack.append(int(x))
        
        return stack[0]