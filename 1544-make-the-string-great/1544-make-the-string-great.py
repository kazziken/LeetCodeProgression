class Solution:
    def makeGood(self, s: str) -> str:
        while len(s) > 1:
            find = False
        
            for i in range(len(s) - 1):
                current_char, next_char = s[i], s[i + 1]

                #if they're a pair, remove them from 's' and let 'find' == True
                if abs(ord(current_char) - ord(next_char)) == 32:
                    s = s[:i] + s[i + 2:]
                    find = True
                    break
            if not find:
                break
        return s
                
        
        
        