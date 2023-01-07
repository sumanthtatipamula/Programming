package Google.GoogleTagProblems;

/*
 * @lc app=leetcode id=739 lang=java
 *
 * [739] Daily Temperatures
 *
 * https://leetcode.com/problems/daily-temperatures/description/
 *
 * algorithms
 * Medium (65.80%)
 * Likes:    5158
 * Dislikes: 139
 * Total Accepted:    290.7K
 * Total Submissions: 440.7K
 * Testcase Example:  '[73,74,75,71,69,72,76,73]'
 *
 * Given an array of integers temperatures represents the daily temperatures,
 * return an array answer such that answer[i] is the number of days you have to
 * wait after the i^th day to get a warmer temperature. If there is no future
 * day for which this is possible, keep answer[i] == 0 instead.
 *
 *
 * Example 1:
 * Input: temperatures = [73,74,75,71,69,72,76,73]
 * Output: [1,1,4,2,1,1,0,0]
 * Example 2:
 * Input: temperatures = [30,40,50,60]
 * Output: [1,1,1,0]
 * Example 3:
 * Input: temperatures = [30,60,90]
 * Output: [1,1,0]
 *
 *
 * Constraints:
 *
 *
 * 1 <= temperatures.length <= 10^5
 * 30 <= temperatures[i] <= 100
 *
 *
 */
import java.util.*;

// @lc code=start
class Solution {

  public int[] dailyTemperatures(int[] temperatures) {
    Stack<Integer[]> st = new Stack<>();
    int result[] = new int[temperatures.length];
    for (int i = temperatures.length - 1; i >= 0; i--) {
      while (!st.isEmpty() && st.peek()[0] <= temperatures[i]) {
        st.pop();
      }
      result[i] = st.isEmpty() ? 0 : st.peek()[1] - i;
      st.push(new Integer[] { temperatures[i], i });
    }
    return result;
  }
}
// @lc code=end
