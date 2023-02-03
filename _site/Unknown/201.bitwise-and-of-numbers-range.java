package Unknown;

/*
 * @lc app=leetcode id=201 lang=java
 *
 * [201] Bitwise AND of Numbers Range
 *
 * https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
 *
 * algorithms
 * Medium (41.27%)
 * Likes:    2588
 * Dislikes: 192
 * Total Accepted:    231.2K
 * Total Submissions: 546.4K
 * Testcase Example:  '5\n7'
 *
 * Given two integers left and right that represent the range [left, right],
 * return the bitwise AND of all numbers in this range, inclusive.
 *
 *
 * Example 1:
 *
 *
 * Input: left = 5, right = 7
 * Output: 4
 *
 *
 * Example 2:
 *
 *
 * Input: left = 0, right = 0
 * Output: 0
 *
 *
 * Example 3:
 *
 *
 * Input: left = 1, right = 2147483647
 * Output: 0
 *
 *
 *
 * Constraints:
 *
 *
 * 0 <= left <= right <= 2^31 - 1
 *
 *
 */

// @lc code=start
class Solution {

  public int rangeBitwiseAnd(int left, int right) {
    if (left == 0) return 0;
    int factor = 1;
    while (left != right) {
      left >>= 1;
      right >>= 1;
      factor <<= 1;
    }
    return left * factor;
  }
}
// @lc code=end
