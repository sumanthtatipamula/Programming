package POD;
import java.util.HashMap;

/*
 * @lc app=leetcode id=1657 lang=java
 *
 * [1657] Determine if Two Strings Are Close
 *
 * https://leetcode.com/problems/determine-if-two-strings-are-close/description/
 *
 * algorithms
 * Medium (54.66%)
 * Likes:    881
 * Dislikes: 52
 * Total Accepted:    48.1K
 * Total Submissions: 88.2K
 * Testcase Example:  '"abc"\n"bca"'
 *
 * Two strings are considered close if you can attain one from the other using
 * the following operations:
 * 
 * 
 * Operation 1: Swap any two existing characters.
 * 
 * 
 * For example, abcde -> aecdb
 * 
 * 
 * Operation 2: Transform every occurrence of one existing character into
 * another existing character, and do the same with the other
 * character.
 * 
 * For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into
 * a's)
 * 
 * 
 * 
 * 
 * You can use the operations on either string as many times as necessary.
 * 
 * Given two strings, word1 and word2, return true if word1 and word2 are
 * close, and false otherwise.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: word1 = "abc", word2 = "bca"
 * Output: true
 * Explanation: You can attain word2 from word1 in 2 operations.
 * Apply Operation 1: "abc" -> "acb"
 * Apply Operation 1: "acb" -> "bca"
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: word1 = "a", word2 = "aa"
 * Output: false
 * Explanation: It is impossible to attain word2 from word1, or vice versa, in
 * any number of operations.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: word1 = "cabbba", word2 = "abbccc"
 * Output: true
 * Explanation: You can attain word2 from word1 in 3 operations.
 * Apply Operation 1: "cabbba" -> "caabbb"
 * Apply Operation 2: "caabbb" -> "baaccc"
 * Apply Operation 2: "baaccc" -> "abbccc"
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= word1.length, word2.length <= 10^5
 * word1 and word2 contain only lowercase English letters.
 * 
 * 
 */

// @lc code=start
class Solution {
    public boolean closeStrings(String word1, String word2) {
        if (word1.length() != word2.length()) {
            return false;
        }
        int[] wf = new int[26];
        int[] wf2 = new int[26];
        for (int i = 0; i < word1.length(); i++) {
            wf[word1.charAt(i) - 'a'] += 1;
            wf2[word2.charAt(i) - 'a'] += 1;
        }
        for( int i = 0; i < 26; i++ ){
           if( wf[i] == 0 && wf2[i] != 0 ) return false;
        }
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < 26; i++) {
            map.put(wf[i], map.getOrDefault(wf[i], 0) + 1);
            map.put(wf2[i], map.getOrDefault(wf2[i], 0) - 1);
        }
        for (var key: map.keySet()) {
            if (map.get(key) != 0) {
                return false;
            }
        }
        return true;
    }
}
// @lc code=end

