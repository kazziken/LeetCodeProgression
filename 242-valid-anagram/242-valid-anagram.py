class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # if s == t:
        #     return False
        
        # if s == t[::-1]
            #return True
        
        sMap, tMap = {} , {}
        
        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i], 0)
            tMap[t[i]] = 1 + tMap.get(t[i], 0)
        # if you return this and its true then returns True
        return sMap == tMap
        