/**
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

 

Example 1:



Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
 

Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9

input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
**/

class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& A, vector<vector<int>>& B) {
        int i = 0, j = 0, a1, a2, b1, b2;
        vector<vector<int>> res;
        while (i < A.size() && j < B.size()) {
            a1 = A[i][0];
            a2 = A[i][1];

            b1 = B[j][0];
            b2 = B[j][1];
            
            if (a1 <= b2 && a2 >= b1) res.push_back(vector<int>{max(a1, b1), min(a2, b2)});
            
            if (a2 > b2) j++;
            else i++;
        }
        
        return res;
    }
};