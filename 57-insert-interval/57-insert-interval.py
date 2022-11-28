class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            #newinterval ending index is less than intervals starting index : so add that first then intervals after
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            #newInterval starting index > intervals ending index so it doesn't overlap
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            #else if they overlap 
            # newInterval takes the min of starting index of both intervals and newIntervals
            # and the max of intervals and newintervals to create the newly formatted newInterval that
            else:
                newInterval = [
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1])
                ]
        res.append(newInterval)
        return res
        