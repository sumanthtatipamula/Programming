/*
 * @lc app=leetcode id=42 lang=java
 *
 * [42] Trapping Rain Water
 *
 * https://leetcode.com/problems/trapping-rain-water/description/
 *
 * algorithms
 * Hard (53.43%)
 * Likes:    14019
 * Dislikes: 197
 * Total Accepted:    874.3K
 * Total Submissions: 1.6M
 * Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
 *
 * Given n non-negative integers representing an elevation map where the width
 * of each bar is 1, compute how much water it can trap after raining.
 *
 *
 * Example 1:
 *
 *
 * Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
 * Output: 6
 * Explanation: The above elevation map (black section) is represented by array
 * [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue
 * section) are being trapped.
 *
 *
 * Example 2:
 *
 *
 * Input: height = [4,2,0,3,2,5]
 * Output: 9
 *
 *
 *
 * Constraints:
 *
 *
 * n == height.length
 * 1 <= n <= 2 * 10^4
 * 0 <= height[i] <= 10^5
 *
 *
 */

// @lc code=start
class Solution {

  public int trap(int[] height) {
    int left_max = 0;
    int right_max = 0;
    int left = 0;
    int right = height.length - 1;
    int water = 0;
    while (left < right) {
      if (height[left] < height[right]) {
        if (height[left] >= left_max) left_max = height[left]; else water +=
          left_max - height[left];
        left++;
      } else {
        if (height[right] >= right_max) right_max = height[right]; else water +=
          right_max - height[right];
        right--;
      }
    }
    return water;
  }

  private int usingExtraSpace(int[] height) {
    int leftMax[] = new int[height.length];
    int rightMax[] = new int[height.length];
    for (int i = 1; i < height.length; i++) {
      leftMax[i] = Math.max(leftMax[i - 1], height[i - 1]);
    }
    for (int i = height.length - 2; i >= 0; i--) {
      rightMax[i] = Math.max(rightMax[i + 1], height[i + 1]);
    }
    int max = 0;
    for (int i = 0; i < height.length; i++) {
      if (height[i] < Math.min(leftMax[i], rightMax[i])) {
        max += Math.min(leftMax[i], rightMax[i]) - height[i];
      }
    }
    return max;
  }
}
// @lc code=end
