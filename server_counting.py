#Given a list of start and end times of server processes, find the highest traffic (# of processes active) and time with the highest number of active processes.
"""
Example input:
times = [
    (1, 5),  # Process 1: starts at 1, ends at 5
    (2, 6),  # Process 2: starts at 2, ends at 6
    (3, 7),  # Process 3: starts at 3, ends at 7
    (5, 8),  # Process 4: starts at 5, ends at 8
    (7, 9)   # Process 5: starts at 7, ends at 9

Output:
(4,5 )
The highest traffic is 4 active processes, occurring at time 5.
"""
class Solution: 
    def highestTraffic(self, times):
        traffic = {}

        for process in times: #correctly grabbed all
            start = process[0]
            end = process[-1]
            #print(start,end) 
            for i in range(start,end+1):
                traffic[i] = traffic.get(i,0)+1
        #print(traffic)

        #getting max time and traffic frequency
        #traffic_dict.items() returns a view object that displays a list of dictionary's key-value tuple pairs
        #key=lambda x: x[1] tells the max function to compare the values (traffic counts) of the dictionary items.  
        maxTime, maxTraffic = max(traffic.items(), key=lambda x: x[1])
        return(maxTime,maxTraffic)

#not the most optimal solution: O(n * R)

#Test cases:
times = [ #should be (5,4)
    (1, 5),  # Process 1: starts at 1, ends at 5
    (2, 6),  # Process 2: starts at 2, ends at 6
    (3, 7),  # Process 3: starts at 3, ends at 7
    (5, 8),  # Process 4: starts at 5, ends at 8
    (7, 9)   # Process 5: starts at 7, ends at 9
]
solution = Solution() 

print(solution.highestTraffic(times))

times = [
    (1, 10),
    (1, 10),
    (1, 10),
    (1, 10)
]
# Expected Output: (1, 4)
# Explanation: All 4 processes are active from time 1 to 10.
print(solution.highestTraffic(times))  # Output should be (1, 4)

times = [
    (1, 2),
    (1, 2),
    (1, 2)
]
# Expected Output: (1, 3)
# Explanation: All 3 processes are active at time 1.
print(solution.highestTraffic(times))  # Output should be (1, 3)


