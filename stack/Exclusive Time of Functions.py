"""
On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n-1.

Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

You are given a list logs, where logs[i] represents the ith log message formatted as a string "{function_id}:{"start" | "end"}:{timestamp}". For example, "0:start:3" means a function call with function ID 0 started at the beginning of timestamp 3, and "1:end:2" means a function call with function ID 1 ended at the end of timestamp 2. Note that a function can be called multiple times, possibly recursively.

A function's exclusive time is the sum of execution times for all function calls in the program. For example, if a function is called twice, one call executing for 2 time units and another call executing for 1 time unit, the exclusive time is 2 + 1 = 3.

Return the exclusive time of each function in an array, where the value at the ith index represents the exclusive time for the function with ID i.

Solution : Stack -> Maintain on stack the current function executed, its start time and its current exec time. Process each log entry, based on start/end.
                    If start, update exectime for the current process on top of stack.
                    If ending, update the startime for the current process on top of stack.

            Time complexity : O(N)
            Space complexity : O(N/2) -> N/2 starts and N/2 stops
           
"""

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = []
        stack = []
        """
        cur = [func_num, start_time, exec_time]
        """
        mx = 0
        hm = {}
        for log in logs:
            func_num, operation, t = log.split(":")
            t = int(t)
            func_num = int(func_num)
            mx = max(mx, func_num)
            if operation == "end":
                end_num, end_start_time, end_exec_time = stack.pop()
                end_exec_time += (t - end_start_time +1)
                hm[end_num] = hm.get(end_num, 0)+ (end_exec_time)
                if stack:
                    stack[-1][1] = t+1
            elif operation == "start":
                if stack:
                    stack[-1][2] += (t - stack[-1][1])
                stack.append([func_num, t, 0])
        for i in range(0, mx+1):
            ans.append(hm[i])
        return ans