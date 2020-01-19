/**
There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

 

Example:

Input: [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]

Output: 2
**/

class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        unordered_map<int, int> counts;
        for (auto w: wall) {
            for (int i = 0; i < w.size()-1; i++) {
                if (i != 0)
                    w[i] += w[i-1];
                
                if (counts.count(w[i])) counts[w[i]]++;
                else counts[w[i]] = 1;
            }
        }
        
        if (counts.size()) {
            int max = -1;
            for (auto i = counts.begin(); i != counts.end(); i++) { 
                if (max < i->second) max = i->second;
            } 
            return wall.size()-max;
        }
        return wall.size();
    }
};