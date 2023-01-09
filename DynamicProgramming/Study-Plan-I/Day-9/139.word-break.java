/*
 * @lc app=leetcode id=139 lang=java
 *
 * [139] Word Break
 *
 * https://leetcode.com/problems/word-break/description/
 *
 * algorithms
 * Medium (43.52%)
 * Likes:    13108
 * Dislikes: 557
 * Total Accepted:    1.3M
 * Total Submissions: 2.8M
 * Testcase Example:  '"leetcode"\n["leet","code"]'
 *
 * Given a string s and a dictionary of strings wordDict, return true if s can
 * be segmented into a space-separated sequence of one or more dictionary
 * words.
 *
 * Note that the same word in the dictionary may be reused multiple times in
 * the segmentation.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "leetcode", wordDict = ["leet","code"]
 * Output: true
 * Explanation: Return true because "leetcode" can be segmented as "leet
 * code".
 *
 *
 * Example 2:
 *
 *
 * Input: s = "applepenapple", wordDict = ["apple","pen"]
 * Output: true
 * Explanation: Return true because "applepenapple" can be segmented as "apple
 * pen apple".
 * Note that you are allowed to reuse a dictionary word.
 *
 *
 * Example 3:
 *
 *
 * Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
 * Output: false
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 300
 * 1 <= wordDict.length <= 1000
 * 1 <= wordDict[i].length <= 20
 * s and wordDict[i] consist of only lowercase English letters.
 * All the strings of wordDict are unique.
 *
 *
 */

import java.util.*;

// @lc code=start
class Solution {
  int memo[];

  public boolean wordBreak(String s, List<String> wordDict) {
    boolean dp[] = new boolean[s.length() + 1];
    dp[s.length()] = true;
    for (int i = s.length() - 1; i >= 0; i--) {
      for (var string : wordDict) {
        if (
          string.length() <= s.length() - i &&
          s.substring(i, i + string.length()).equals(string) &&
          !dp[i]
        ) {
          dp[i] = dp[i + string.length()];
        }
      }
    }
    return dp[0];
  }

  private boolean recursiveSolution(String s, List<String> wordDict) {
    HashSet<String> dictMap = new HashSet<>();
    memo = new int[s.length()];
    Arrays.fill(memo, -1);
    for (int i = 0; i < wordDict.size(); i++) {
      dictMap.add(wordDict.get(i));
    }
    return wordBreak(s, 0, dictMap);
  }

  private boolean wordBreak(String s, int index, HashSet<String> dictMap) {
    if (index == s.length()) return true;
    if (memo[index] > -1) return memo[index] == 0 ? false : true;
    StringBuffer sb = new StringBuffer();
    for (int i = index; i < s.length(); i++) {
      sb.append(s.charAt(i));
      if (dictMap.contains(sb.toString()) && wordBreak(s, i + 1, dictMap)) {
        return true;
      }
    }
    memo[index] = 0;
    return false;
  }
}
// @lc code=end
