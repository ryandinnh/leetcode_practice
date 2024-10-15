class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: #while current temperature is greater than either the latest temp or top of the stack, stack[-1][0] as the stack has tuple pairs (temperature,index) so you only want to access temp
                stackT, stackI = stack.pop() 
                out[stackI] = i - stackI
            stack.append((t, i))
        
        return out