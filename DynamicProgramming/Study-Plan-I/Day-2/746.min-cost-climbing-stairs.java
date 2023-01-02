/*
 * @lc app=leetcode id=746 lang=java
 *
 * [746] Min Cost Climbing Stairs
 *
 * https://leetcode.com/problems/min-cost-climbing-stairs/description/
 *
 * algorithms
 * Easy (54.47%)
 * Likes:    4271
 * Dislikes: 843
 * Total Accepted:    307.6K
 * Total Submissions: 559.3K
 * Testcase Example:  '[10,15,20]'
 *
 * You are given an integer array cost where cost[i] is the cost of i^th step
 * on a staircase. Once you pay the cost, you can either climb one or two
 * steps.
 *
 * You can either start from the step with index 0, or the step with index 1.
 *
 * Return the minimum cost to reach the top of the floor.
 *
 *
 * Example 1:
 *
 *
 * Input: cost = [10,15,20]
 * Output: 15
 * Explanation: Cheapest is: start on cost[1], pay that cost, and go to the
 * top.
 *
 *
 * Example 2:
 *
 *
 * Input: cost = [1,100,1,1,1,100,1,1,100,1]
 * Output: 6
 * Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping
 * cost[3].
 *
 *
 *
 * Constraints:
 *
 *
 * 2 <= cost.length <= 1000
 * 0 <= cost[i] <= 999
 *
 *
 */

// @lc code=start
class Solution {

  public int minCostClimbingStairs(int[] cost) {
    int n = cost.length;
    int first = cost[0];
    int second = cost[1];
    if (n <= 2) return Math.min(first, second);
    for (int i = 2; i < n; i++) {
      int curr = cost[i] + Math.min(first, second);
      first = second;
      second = curr;
    }
    return Math.min(first, second);
  }
}
// @lc code=end
