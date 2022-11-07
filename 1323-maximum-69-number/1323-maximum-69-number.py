class Solution:
    def maximum69Number (self, num: int) -> int:
        """
        Loop through the number
        Find the first 6 and swapping it to be a 9
        
        """
        
        
        numList = list(str(num)) #ex. 669 -> [6,6,9]
        
        for i, current_char in enumerate(numList):
            # find first 6 then turn it into a 9 then break the loop
            if current_char == '6':
                numList[i] = '9'
                break
        return int("".join(numList))
        
        