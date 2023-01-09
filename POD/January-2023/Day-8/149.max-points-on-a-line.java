import java.util.HashMap;

/*
 * @lc app=leetcode id=149 lang=java
 *
 * [149] Max Points on a Line
 *
 * https://leetcode.com/problems/max-points-on-a-line/description/
 *
 * algorithms
 * Hard (19.40%)
 * Likes:    1834
 * Dislikes: 268
 * Total Accepted:    266.8K
 * Total Submissions: 1.2M
 * Testcase Example:  '[[1,1],[2,2],[3,3]]'
 *
 * Given an array of points where points[i] = [xi, yi] represents a point on
 * the X-Y plane, return the maximum number of points that lie on the same
 * straight line.
 *
 *
 * Example 1:
 *
 *
 * Input: points = [[1,1],[2,2],[3,3]]
 * Output: 3
 *
 *
 * Example 2:
 *
 *
 * Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
 * Output: 4
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= points.length <= 300
 * points[i].length == 2
 * -10^4 <= xi, yi <= 10^4
 * All the points are unique.
 *
 *
 */

// @lc code=start
class Solution {

  public int maxPoints(int[][] points) {
    int maxPoints = 0;
    for (int i = 0; i < points.length; i++) {
      int x1 = points[i][0];
      int y1 = points[i][1];
      HashMap<Float, Integer> slopesCount = new HashMap<>();
      for (int j = i + 1; j < points.length; j++) {
        int x2 = points[j][0];
        int y2 = points[j][1];
        float slope = 0;
        if (x1 == x2) {
          slope = Float.POSITIVE_INFINITY;
        } else if (y2 != y1) {
          slope = (float) (y2 - y1) / (x2 - x1);
        }
        slopesCount.put(slope, slopesCount.getOrDefault(slope, 0) + 1);
        maxPoints = Math.max(maxPoints, slopesCount.get(slope));
      }
    }
    return maxPoints + 1;
  }
}
// @lc code=end
