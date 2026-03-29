class Solution:
    def minOperations(self, logs: List[str]) -> int:
        #understand: stack
        #plan: put in the stack, then pop when those found.
        #append things. pass when ./ , pop when ../
        #edge cases:
        #imp:
        #diff of len(range(something)) and for nums in num:

        stack = []

        for log in logs:
            if log == '../':
                if stack:
                    stack.pop()
            elif log == './':
                continue
            else:
                stack.append(log)
                
        
        return len(stack)