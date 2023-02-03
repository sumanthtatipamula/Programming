/*
 * @lc app=leetcode id=918 lang=java
 *
 * [918] Maximum Sum Circular Subarray
 *
 * https://leetcode.com/problems/maximum-sum-circular-subarray/description/
 *
 * algorithms
 * Medium (35.83%)
 * Likes:    3981
 * Dislikes: 181
 * Total Accepted:    145.4K
 * Total Submissions: 379.4K
 * Testcase Example:  '[1,-2,3,-2]'
 *
 * Given a circular integer array nums of length n, return the maximum possible
 * sum of a non-empty subarray of nums.
 *
 * A circular array means the end of the array connects to the beginning of the
 * array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the
 * previous element of nums[i] is nums[(i - 1 + n) % n].
 *
 * A subarray may only include each element of the fixed buffer nums at most
 * once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there
 * does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,-2,3,-2]
 * Output: 3
 * Explanation: Subarray [3] has maximum sum 3.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [5,-3,5]
 * Output: 10
 * Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [-3,-2,-3]
 * Output: -2
 * Explanation: Subarray [-2] has maximum sum -2.
 *
 *
 *
 * Constraints:
 *
 *
 * n == nums.length
 * 1 <= n <= 3 * 10^4
 * -3 * 10^4 <= nums[i] <= 3 * 10^4
 *
 *
 */

// @lc code=start
class Solution {

  public int maxSubarraySumCircular(int[] nums) {
    int maxSum = Integer.MIN_VALUE;
    int minSum = Integer.MAX_VALUE;
    int currMax = 0;
    int currMin = 0;
    int total = 0;
    for (int i = 0; i < nums.length; i++) {
      currMax = Math.max(currMax + nums[i], nums[i]);
      currMin = Math.min(currMin + nums[i], nums[i]);
      maxSum = Math.max(maxSum, currMax);
      minSum = Math.min(minSum, currMin);
      total += nums[i];
    }
    return maxSum < 0 ? maxSum : Math.max(maxSum, total - minSum);
  }
}
// @lc code=end
