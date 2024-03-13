#not correct solution
class Solution:
    def insert(self, intervals, newInterval):
        final_array = []
        currStart = newInterval[0]
        currEnd = newInterval[1]

        for i in range(len(intervals)):
            interStart = intervals[i][0]
            interEnd = intervals[i][1]

            #check to see if there are any overlaps
            if currEnd < interStart:
                #means there is no overlap
                final_array.append([currStart, currEnd])
                return final_array + intervals[i:]
            elif currStart > interEnd:
                final_array.append(intervals[i])
            
            else:
                #there is an interval
                currStart = min(currStart, interStart) 
                currEnd  = max(currEnd, interEnd)
                
            
        final_array.append([currStart, currEnd])
        return final_array


class Solution:
    def insert(self, intervals, newInterval):
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                #is overlapping
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        return res