class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        
        for c in s:
            if c in dict:
                top = stack.pop() if stack else '#'
                if top != dict[c]:
                    return False
            else:
                stack.append(c)
        return stack == []