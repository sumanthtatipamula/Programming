package Google.GoogleTagProblems;

/*
 * @lc app=leetcode id=347 lang=java
 *
 * [347] Top K Frequent Elements
 *
 * https://leetcode.com/problems/top-k-frequent-elements/description/
 *
 * algorithms
 * Medium (63.90%)
 * Likes:    12319
 * Dislikes: 455
 * Total Accepted:    1.3M
 * Total Submissions: 2M
 * Testcase Example:  '[1,1,1,2,2,3]\n2'
 *
 * Given an integer array nums and an integer k, return the k most frequent
 * elements. You may return the answer in any order.
 *
 *
 * Example 1:
 * Input: nums = [1,1,1,2,2,3], k = 2
 * Output: [1,2]
 * Example 2:
 * Input: nums = [1], k = 1
 * Output: [1]
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 10^5
 * -10^4 <= nums[i] <= 10^4
 * k is in the range [1, the number of unique elements in the array].
 * It is guaranteed that the answer is unique.
 *
 *
 *
 * Follow up: Your algorithm's time complexity must be better than O(n log n),
 * where n is the array's size.
 *
 */

import java.util.*;

// @lc code=start
class Solution {

  class Pair {
    int num;
    int count;

    Pair(int num, int count) {
      this.num = num;
      this.count = count;
    }
  }

  public int[] topKFrequent(int[] nums, int k) {
    HashMap<Integer, Integer> map = new HashMap<>();
    for (var num : nums) {
      map.put(num, map.getOrDefault(num, 0) + 1);
    }
    PriorityQueue<Pair> pq = new PriorityQueue<>(
      (p1, p2) -> {
        if (p1.count == p2.count) {
          return Integer.compare(p1.num, p2.num);
        }
        return Integer.compare(p2.count, p1.count);
      }
    );
    map.forEach(
      (num, count) -> {
        pq.add(new Pair(num, count));
      }
    );
    int[] result = new int[k];
    for (int i = 0; i < k; i++) {
      result[i] = pq.poll().num;
    }
    return result;
  }
}
// @lc code=end
