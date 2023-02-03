/*
 * @lc app=leetcode id=53 lang=java
 *
 * [53] Maximum Subarray
 *
 * https://leetcode.com/problems/maximum-subarray/description/
 *
 * algorithms
 * Easy (48.48%)
 * Likes:    14611
 * Dislikes: 683
 * Total Accepted:    1.7M
 * Total Submissions: 3.4M
 * Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
 *
 * Given an integer array nums, find the contiguous subarray (containing at
 * least one number) which has the largest sum and return its sum.
 *
 * A subarray is a contiguous part of an array.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
 * Output: 6
 * Explanation: [4,-1,2,1] has the largest sum = 6.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [1]
 * Output: 1
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [5,4,-1,7,8]
 * Output: 23
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 3 * 10^4
 * -10^5 <= nums[i] <= 10^5
 *
 *
 *
 * Follow up: If you have figured out the O(n) solution, try coding another
 * solution using the divide and conquer approach, which is more subtle.
 *
 */

// @lc code=start
class Solution {

  public int maxSubArray(int[] nums) {
    int maxSum = Integer.MIN_VALUE;
    int currSum = 0;
    for (int i = 0; i < nums.length; i++) {
      currSum = Math.max(currSum + nums[i], nums[i]);
      maxSum = Math.max(maxSum, currSum);
      if (currSum < 0) {
        currSum = 0;
      }
    }
    return maxSum;
  }
}
// @lc code=end
