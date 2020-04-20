/**
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
**/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int b_i_0 = 0, b_i_1 = INT_MIN, dp_pre_0 = 0, tmp;
        for (int i = 0; i < prices.size(); i++) {
            tmp = b_i_0;
            b_i_0 = max(b_i_0, b_i_1+prices[i]);
            b_i_1 = max(b_i_1, dp_pre_0-prices[i]);
            dp_pre_0 = tmp;
        }
        return b_i_0;
    }
};