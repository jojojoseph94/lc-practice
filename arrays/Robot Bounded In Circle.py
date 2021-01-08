"""
On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

Example 1:

Input: "GGLLGG"
Output: true
Explanation: 
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:

Input: "GG"
Output: false
Explanation: 
The robot moves north indefinitely.
Example 3:

Input: "GL"
Output: true
Explanation: 
The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
 

Note:

1 <= instructions.length <= 100
instructions[i] is in {'G', 'L', 'R'}

Solution : Start with robot facing north and origin. After running through the instructions, if the robot returns to the initial position or it does not face north, then there will be a loop. (Alternatively just run through the instrucitons 4 times and see if you get back to the initial state)

            Time complexity : O(N)
            Space complexity : O(1)
"""

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        def move(i,j, direction, ins):
            #up down left right
            moves = [[-1,0], [1,0], [0,-1], [0,1]]
            new_dirs = [{"L": 2, "R": 3}, {"L": 3, "R": 2}, {"L": 1, "R": 0}, {"L": 0, "R": 1}]
            if ins == "G":
                i+=moves[direction][0]
                j+=moves[direction][1]
            elif ins == "L":
                direction = new_dirs[direction]["L"]
            elif ins == "R":
                direction = new_dirs[direction]["R"]
            return (i,j,direction)
                
        times = 0
        i = 0
        j = 0
        direction = 0
        for inst in instructions:
            i,j,direction = move(i,j,direction,inst)
        if (i == 0 and j == 0) or direction != 0:
            return True
        return False