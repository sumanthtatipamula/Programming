package POD;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

import javax.naming.spi.DirStateFactory.Result;

/*
 * @lc app=leetcode id=451 lang=java
 *
 * [451] Sort Characters By Frequency
 *
 * https://leetcode.com/problems/sort-characters-by-frequency/description/
 *
 * algorithms
 * Medium (66.93%)
 * Likes:    5338
 * Dislikes: 205
 * Total Accepted:    424.6K
 * Total Submissions: 616K
 * Testcase Example:  '"tree"'
 *
 * Given a string s, sort it in decreasing order based on the frequency of the
 * characters. The frequency of a character is the number of times it appears
 * in the string.
 * 
 * Return the sorted string. If there are multiple answers, return any of
 * them.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "tree"
 * Output: "eert"
 * Explanation: 'e' appears twice while 'r' and 't' both appear once.
 * So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid
 * answer.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "cccaaa"
 * Output: "aaaccc"
 * Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and
 * "aaaccc" are valid answers.
 * Note that "cacaca" is incorrect, as the same characters must be together.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "Aabb"
 * Output: "bbAa"
 * Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
 * Note that 'A' and 'a' are treated as two different characters.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 5 * 10^5
 * s consists of uppercase and lowercase English letters and digits.
 * 
 * 
 */

// @lc code=start
class Solution {
    public String frequencySort(String s) {
        HashMap<Character, StringBuffer> words = new HashMap<>();
        HashMap<Character, Integer> freq = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if (!words.containsKey(s.charAt(i))) {
                words.put(s.charAt(i), new StringBuffer());
            }
            words.get(s.charAt(i)).append(s.charAt(i));
            freq.put(s.charAt(i), freq.getOrDefault(s.charAt(i), 0) + 1);
        }
        ArrayList<Map.Entry<Character, Integer>> al = new ArrayList<>();
        for (var entry : freq.entrySet()) {
            al.add(entry);
        }
        Collections.sort(
            al,
            (a, b) -> {
                if (a.getValue() != b.getValue()) {
                    return Integer.compare(b.getValue(), a.getValue());
                }
                return 0;
            }
        );
        StringBuffer result = new StringBuffer();
        for (var p : al) {
            result.append(words.get(p.getKey()));
        }
        return result.toString();
    }
}
// @lc code=end

