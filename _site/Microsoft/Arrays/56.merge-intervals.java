package Microsoft.Arrays;
/*
 * @lc app=leetcode id=56 lang=java
 *
 * [56] Merge Intervals
 *
 * https://leetcode.com/problems/merge-intervals/description/
 *
 * algorithms
 * Medium (42.69%)
 * Likes:    9663
 * Dislikes: 435
 * Total Accepted:    1.1M
 * Total Submissions: 2.5M
 * Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
 *
 * Given an array of intervals where intervals[i] = [starti, endi], merge all
 * overlapping intervals, and return an array of the non-overlapping intervals
 * that cover all the intervals in the input.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
 * Output: [[1,6],[8,10],[15,18]]
 * Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
 * [1,6].
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: intervals = [[1,4],[4,5]]
 * Output: [[1,5]]
 * Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= intervals.length <= 10^4
 * intervals[i].length == 2
 * 0 <= starti <= endi <= 10^4
 * 
 * 
 */

import java.util.ArrayList;
import java.util.Arrays;

// @lc code=start
class Solution {
    public int[][] merge(int[][] intervals) {
        ArrayList<int[]> tmp = new ArrayList<>();
        Arrays.sort(intervals, (a, b) ->{
            if(a[0] == b[0]){
                return Integer.compare(a[1], b[1]);
            }
            return Integer.compare(a[0],b[0]);
        });
        int interval[] = intervals[0];
        for (int i = 1; i < intervals.length; i++) {
            if (interval[1] < intervals[i][0]) {
                tmp.add(interval);
                interval = intervals[i];
            } else {
                interval[1] = Math.max(interval[1], intervals[i][1]);
            }
        }
        tmp.add(interval);
        int[][] result = new int[tmp.size()][];
        for (int i = 0; i < tmp.size(); i++) {
            result[i] = tmp.get(i);
        }
        return result;
    }
}
// @lc code=end

