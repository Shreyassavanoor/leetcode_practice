'''
    Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
    
    Example 1:
    Intervals: [[1,4], [2,5], [7,9]]
    Output: [[1,5], [7,9]]
    Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into one [1,5].
    
    Example 2:
    Intervals: [[6,7], [2,4], [5,9]]
    Output: [[2,4], [5,9]]
    Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].
    
    Example 3:
    Intervals: [[1,4], [2,6], [3,5]]
    Output: [[1,6]]
    Explanation: Since all the given intervals overlap, we merged them into one.
'''
from operator   import itemgetter 
def sort_intervals(intervals):
    return sorted(intervals, key=itemgetter(0))

def merge_interval(intervals):
    if len(intervals) < 2:
        print(intervals)
        return
    
    result = []
    
    #step 1: sort the intervals
    sorted_intervals = sort_intervals(intervals)
    
    #step2: compare start and end time of intervals
    start = sorted_intervals[0][0]
    end = sorted_intervals[0][1]
    
    for i in range(1, len(sorted_intervals)):
        interval = sorted_intervals[i]
        if interval[0] <= end:
            end = max(end, interval[1])
        else:
           result.append([start, end])
           start = interval[0]
           end = interval[1]
    
    result.append([start, end])
    
    for i in result:
        print(i, end='')
    print('/n') 

if __name__ == '__main__':
    merge_interval([[1,4], [2,5], [7,9]])
    merge_interval([[6,7], [2,4], [5,9]])
    merge_interval([[1,4], [2,6], [3,5]])