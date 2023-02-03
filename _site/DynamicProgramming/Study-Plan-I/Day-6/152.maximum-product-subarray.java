/*
 * @lc app=leetcode id=152 lang=java
 *
 * [152] Maximum Product Subarray
 *
 * https://leetcode.com/problems/maximum-product-subarray/description/
 *
 * algorithms
 * Medium (33.72%)
 * Likes:    14758
 * Dislikes: 440
 * Total Accepted:    929.5K
 * Total Submissions: 2.7M
 * Testcase Example:  '[2,3,-2,4]'
 *
 * Given an integer array nums, find a subarray that has the largest product,
 * and return the product.
 *
 * The test cases are generated so that the answer will fit in a 32-bit
 * integer.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [2,3,-2,4]
 * Output: 6
 * Explanation: [2,3] has the largest product 6.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [-2,0,-1]
 * Output: 0
 * Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 2 * 10^4
 * -10 <= nums[i] <= 10
 * The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
 * integer.
 *
 *
 */

// @lc code=start
class Solution {

  public int maxProduct(int[] nums) {
    int min_ending_here = 1;
    int max_ending_here = 1;
    int max_so_far = Integer.MIN_VALUE;
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] < 0) {
        int tmp = min_ending_here;
        min_ending_here = max_ending_here;
        max_ending_here = tmp;
      }
      min_ending_here = Math.min(min_ending_here * nums[i], nums[i]);
      max_ending_here = Math.max(max_ending_here * nums[i], nums[i]);
      max_so_far = Math.max(max_ending_here, max_so_far);
    }
    return max_so_far;
  }
}
// @lc code=end
