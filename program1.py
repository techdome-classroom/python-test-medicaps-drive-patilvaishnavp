class Solution(object):
    def isValid(self, s):
        def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)
        return not stack

# Example usage:
solution = Solution()
print(solution.isValid("()"))      
print(solution.isValid("()[]{}"))  
print(solution.isValid("(]"))      

        pass
    



  

