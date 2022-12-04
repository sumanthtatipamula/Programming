package Microsoft.Arrays;
/*
 * @lc app=leetcode id=344 lang=java
 *
 * [344] Reverse String
 *
 * https://leetcode.com/problems/reverse-string/description/
 *
 * algorithms
 * Easy (71.90%)
 * Likes:    2960
 * Dislikes: 832
 * Total Accepted:    1.2M
 * Total Submissions: 1.6M
 * Testcase Example:  '["h","e","l","l","o"]'
 *
 * Write a function that reverses a string. The input string is given as an
 * array of characters s.
 * 
 * 
 * Example 1:
 * Input: s = ["h","e","l","l","o"]
 * Output: ["o","l","l","e","h"]
 * Example 2:
 * Input: s = ["H","a","n","n","a","h"]
 * Output: ["h","a","n","n","a","H"]
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 10^5
 * s[i] is a printable ascii character.
 * 
 * 
 * 
 * Follow up: Do not allocate extra space for another array. You must do this
 * by modifying the input array in-place with O(1) extra memory.
 * 
 */

// @lc code=start
class Solution {
    public void reverseString(char[] s) {
        int i = 0;
        int j = s.length - 1;
        while (i < j) {
            char tmp = s[i];
            s[i++] = s[j];
            s[j--] = tmp;
        }
    }
}
// @lc code=end

