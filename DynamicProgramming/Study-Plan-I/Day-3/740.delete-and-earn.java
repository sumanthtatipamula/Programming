/*
 * @lc app=leetcode id=740 lang=java
 *
 * [740] Delete and Earn
 *
 * https://leetcode.com/problems/delete-and-earn/description/
 *
 * algorithms
 * Medium (53.91%)
 * Likes:    5994
 * Dislikes: 319
 * Total Accepted:    247.6K
 * Total Submissions: 432.4K
 * Testcase Example:  '[3,4,2]'
 *
 * You are given an integer array nums. You want to maximize the number of
 * points you get by performing the following operation any number of
 * times:
 *
 *
 * Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must
 * delete every element equal to nums[i] - 1 and every element equal to nums[i]
 * + 1.
 *
 *
 * Return the maximum number of points you can earn by applying the above
 * operation some number of times.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [3,4,2]
 * Output: 6
 * Explanation: You can perform the following operations:
 * - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
 * - Delete 2 to earn 2 points. nums = [].
 * You earn a total of 6 points.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [2,2,3,3,3,4]
 * Output: 9
 * Explanation: You can perform the following operations:
 * - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums =
 * [3,3].
 * - Delete a 3 again to earn 3 points. nums = [3].
 * - Delete a 3 once more to earn 3 points. nums = [].
 * You earn a total of 9 points.
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 2 * 10^4
 * 1 <= nums[i] <= 10^4
 *
 *
 */
import java.util.*;

// @lc code=start
class Solution {

  public int deleteAndEarn(int[] nums) {
    ArrayList<Integer> unique = new ArrayList<>();
    HashMap<Integer, Integer> profit = new HashMap<>();
    Arrays.sort(nums);
    for (int i = 0; i < nums.length; i++) {
      if (!profit.containsKey(nums[i])) {
        unique.add(nums[i]);
        profit.put(nums[i], 0);
      }
      profit.put(nums[i], profit.get(nums[i]) + nums[i]);
    }
    int pprev = 0;
    int prev = profit.get(unique.get(0));
    for (int i = 1; i < unique.size(); i++) {
      int tmp = prev;
      if (unique.get(i) == unique.get(i - 1) + 1) {
        prev = Math.max(pprev + profit.get(unique.get(i)), prev);
      } else {
        prev += profit.get(unique.get(i));
      }
      pprev = tmp;
    }
    return Math.max(pprev, prev);
  }
}
// @lc code=end
