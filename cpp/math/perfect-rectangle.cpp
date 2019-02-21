/**
Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).

Example 1:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

Return true. All 5 rectangles together form an exact cover of a rectangular region.

Example 2:

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions.

Example 3:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.

Example 4:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.
 * **/

#include <vector>
#include <set>
#include <string>
#include <algorithm>

class Solution
{
  public:
    bool isRectangleCover(std::vector<std::vector<int>> &rectangles)
    {
        if (rectangles.size() == 0 || rectangles[0].size() != 4)
            return false;
        std::set<std::string> s;
        int leftx = INT_MAX, lefty = INT_MAX, rightx = INT_MIN, righty = INT_MIN;
        int area = 0;
        for (auto &rec : rectangles)
        {

            int x1 = rec[0];
            int y1 = rec[1];
            int x2 = rec[2];
            int y2 = rec[3];

            leftx = std::min(leftx, x1);
            lefty = std::min(lefty, y1);
            rightx = std::max(rightx, x2);
            righty = std::max(righty, y2);

            area += (x2 - x1) * (y2 - y1);
            std::string sx1 = std::to_string(x1), sy1 = std::to_string(y1), sx2 = std::to_string(x2), sy2 = std::to_string(y2);
            auto res_1 = s.insert(sx1 + " " + sy1);
            if (!res_1.second)
                s.erase(res_1.first);

            auto res_2 = s.insert(sx1 + " " + sy2);
            if (!res_2.second)
                s.erase(res_2.first);

            auto res_3 = s.insert(sx2 + " " + sy1);
            if (!res_3.second)
                s.erase(res_3.first);

            auto res_4 = s.insert(sx2 + " " + sy2);
            if (!res_4.second)
                s.erase(res_4.first);
        }

        if (s.find(std::to_string(leftx) + " " + std::to_string(lefty)) == s.end() || s.find(std::to_string(leftx) + " " + std::to_string(righty)) == s.end() || s.find(std::to_string(rightx) + " " + std::to_string(lefty)) == s.end() || s.find(std::to_string(rightx) + " " + std::to_string(righty)) == s.end() || s.size() != 4)
            return false;

        return (rightx - leftx) * (righty - lefty) == area;
    }
};