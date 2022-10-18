class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict:
                top = stack.pop() if stack else '#'
                
                if top != dict[char]:
                    return False
            else:
                stack.append(char)
        return stack == []
        
        