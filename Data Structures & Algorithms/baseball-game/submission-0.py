class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #understand
        #operations. 
        #plan
        #stack
        #imp
        stack = []

        for op in operations:
            if op == '+':
                summ = stack[-1] + stack[-2] 
                stack.append(summ)
            elif op == 'D':
                double = stack[-1] * 2
                stack.append(double)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)