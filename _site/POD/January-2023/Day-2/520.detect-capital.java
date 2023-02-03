/*
 * @lc app=leetcode id=520 lang=java
 *
 * [520] Detect Capital
 *
 * https://leetcode.com/problems/detect-capital/description/
 *
 * algorithms
 * Easy (54.18%)
 * Likes:    920
 * Dislikes: 308
 * Total Accepted:    203.3K
 * Total Submissions: 375.1K
 * Testcase Example:  '"USA"'
 *
 * We define the usage of capitals in a word to be right when one of the
 * following cases holds:
 *
 *
 * All letters in this word are capitals, like "USA".
 * All letters in this word are not capitals, like "leetcode".
 * Only the first letter in this word is capital, like "Google".
 *
 *
 * Given a string word, return true if the usage of capitals in it is right.
 *
 *
 * Example 1:
 * Input: word = "USA"
 * Output: true
 * Example 2:
 * Input: word = "FlaG"
 * Output: false
 *
 *
 * Constraints:
 *
 *
 * 1 <= word.length <= 100
 * word consists of lowercase and uppercase English letters.
 *
 *
 */

// @lc code=start
class Solution {

  public boolean detectCapitalUse(String word) {
    if (word.toUpperCase().equals(word)) {
      return true;
    } else if (
      word.charAt(0) <= 90 &&
      word.substring(1).equals(word.substring(1).toLowerCase())
    ) {
      return true;
    } else if (word.toLowerCase().equals(word)) {
      return true;
    }
    return false;
  }
}
// @lc code=end
