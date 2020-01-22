/**
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

 

Example 1:

Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:

Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
**/

class Solution {
public:
    int minAreaRect(vector<vector<int>>& points) {
        unordered_map<int, unordered_set<int>> u_map;
        for (auto p: points) {
            if (u_map.count(p[0])) u_map[p[0]].insert(p[1]);
            else u_map[p[0]] = unordered_set<int>{p[1]};
        }
        
        if (u_map.size() == points.size()) return 0;
        
        int min_area = INT_MAX;
        for (auto p: points) {
            int x1 = p[0], y1 = p[1];
            for (auto p: points) {
                int x2 = p[0], y2 = p[1];
                if (x2 != x1 && y1 != y2 && u_map[x1].count(y2) && u_map[x2].count(y1)) 
                    min_area = min(min_area, abs(x2-x1)*abs(y2-y1));
            }
        }
        
        return min_area == INT_MAX ? 0:min_area;
    }
};