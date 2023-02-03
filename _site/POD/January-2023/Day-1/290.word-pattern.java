import java.util.HashMap;

/*
 * @lc app=leetcode id=290 lang=java
 *
 * [290] Word Pattern
 *
 * https://leetcode.com/problems/word-pattern/description/
 *
 * algorithms
 * Easy (38.83%)
 * Likes:    2211
 * Dislikes: 251
 * Total Accepted:    277.8K
 * Total Submissions: 714.3K
 * Testcase Example:  '"abba"\n"dog cat cat dog"'
 *
 * Given a pattern and a string s, find if s follows the same pattern.
 *
 * Here follow means a full match, such that there is a bijection between a
 * letter in pattern and a non-empty word in s.
 *
 *
 * Example 1:
 *
 *
 * Input: pattern = "abba", s = "dog cat cat dog"
 * Output: true
 *
 *
 * Example 2:
 *
 *
 * Input: pattern = "abba", s = "dog cat cat fish"
 * Output: false
 *
 *
 * Example 3:
 *
 *
 * Input: pattern = "aaaa", s = "dog cat cat dog"
 * Output: false
 *
 *
 * Example 4:
 *
 *
 * Input: pattern = "abba", s = "dog dog dog dog"
 * Output: false
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= pattern.length <= 300
 * pattern contains only lower-case English letters.
 * 1 <= s.length <= 3000
 * s contains only lower-case English letters and spaces ' '.
 * s does not contain any leading or trailing spaces.
 * All the words in s are separated by a single space.
 *
 *
 */

// @lc code=start
class Solution {

  public boolean wordPattern(String pattern, String s) {
    String words[] = s.split(" ");
    if (words.length != pattern.length()) {
      return false;
    }
    HashMap<Character, String> map = new HashMap<>();
    HashMap<String, Character> wordHashMap = new HashMap<>();
    for (int i = 0; i < pattern.length(); i++) {
      if (
        map.containsKey(pattern.charAt(i)) &&
        !map.get(pattern.charAt(i)).equals(words[i])
      ) {
        return false;
      } else if (
        wordHashMap.containsKey(words[i]) &&
        wordHashMap.get(words[i]) != pattern.charAt(i)
      ) {
        return false;
      }
      map.put(pattern.charAt(i), words[i]);
      wordHashMap.put(words[i], pattern.charAt(i));
    }
    return true;
  }
}
// @lc code=end
