package Google.GoogleTagProblems;

/*
 * @lc app=leetcode id=62 lang=java
 *
 * [62] Unique Paths
 *
 * https://leetcode.com/problems/unique-paths/description/
 *
 * algorithms
 * Medium (58.68%)
 * Likes:    12683
 * Dislikes: 366
 * Total Accepted:    1.3M
 * Total Submissions: 2M
 * Testcase Example:  '3\n7'
 *
 * There is a robot on an m x n grid. The robot is initially located at the
 * top-left corner (i.e., grid[0][0]). The robot tries to move to the
 * bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move
 * either down or right at any point in time.
 *
 * Given the two integers m and n, return the number of possible unique paths
 * that the robot can take to reach the bottom-right corner.
 *
 * The test cases are generated so that the answer will be less than or equal
 * to 2 * 10^9.
 *
 *
 * Example 1:
 *
 *
 * Input: m = 3, n = 7
 * Output: 28
 *
 *
 * Example 2:
 *
 *
 * Input: m = 3, n = 2
 * Output: 3
 * Explanation: From the top-left corner, there are a total of 3 ways to reach
 * the bottom-right corner:
 * 1. Right -> Down -> Down
 * 2. Down -> Down -> Right
 * 3. Down -> Right -> Down
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= m, n <= 100
 *
 *
 */
import java.util.*;

// @lc code=start
class Solution {

  public int uniquePaths(int m, int n) {
    // return recursiveApproach(m, n);
    int dp[][] = new int[m][n];
    dp[m - 1][n - 1] = 1;
    for (int i = 0; i < m; i++) {
      dp[i][0] = 1;
    }
    for (int i = 0; i < m; i++) {
      dp[0][i] = 1;
    }
    for (int i = 1; i < m; i++) {
      for (int j = 1; j < n; j++) {
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
      }
    }
    return dp[m - 1][n - 1];
  }

  private int recursiveApproach(int m, int n) {
    int[][] count = new int[m][n];
    for (int i = 0; i < count.length; i++) {
      Arrays.fill(count[i], -1);
    }
    return uniquePaths(0, 0, count, m, n);
  }

  private int uniquePaths(int i, int j, int[][] count, int m, int n) {
    if (i < 0 || j < 0 || i >= m || j >= n) return 0;
    if (i == m - 1 && j == n - 1) {
      return 1;
    }
    if (count[i][j] > -1) {
      return count[i][j];
    }
    count[i][j] =
      (uniquePaths(i + 1, j, count, m, n) + uniquePaths(i, j + 1, count, m, n));
    return count[i][j];
  }
}
// @lc code=end
