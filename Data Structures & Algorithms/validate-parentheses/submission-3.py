class Solution:
    def isValid(self, s: str) -> bool:
        # make a stack
        #if we find open, put to stack
        #if we find close:
            #if matches stack[-1], we pop
        #return if stack empty
        
        
        stack = []
        closeToOpen = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if stack and char in closeToOpen:
                if closeToOpen[char] == stack[-1]:
                    stack.pop() 
                else:
                    return False

            else:
                stack.append(char)

        return not stack