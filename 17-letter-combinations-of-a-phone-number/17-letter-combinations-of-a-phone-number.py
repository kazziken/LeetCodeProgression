class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno' , '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
        }
        
        # cmb = [''] if digits else []
        # for d in digits:
        #     cmb = [p + q for p in cmb for q in mapping[d]] #loop counter
        # return cmb
        
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])
        prev = self.letterCombinations(digits[:-1]) #all the elements except last one
        additional = mapping[digits[-1]] #last element of digit
        return [s + c for s in prev for c in additional] # loop counter
    