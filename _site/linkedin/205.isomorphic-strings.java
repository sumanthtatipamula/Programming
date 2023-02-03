import java.util.HashMap;

/*
 * @lc app=leetcode id=205 lang=java
 *
 * [205] Isomorphic Strings
 *
 * https://leetcode.com/problems/isomorphic-strings/description/
 *
 * algorithms
 * Easy (41.47%)
 * Likes:    2707
 * Dislikes: 554
 * Total Accepted:    426.2K
 * Total Submissions: 1M
 * Testcase Example:  '"egg"\n"add"'
 *
 * Given two strings s and t, determine if they are isomorphic.
 * 
 * Two strings s and t are isomorphic if the characters in s can be replaced to
 * get t.
 * 
 * All occurrences of a character must be replaced with another character while
 * preserving the order of characters. No two characters may map to the same
 * character, but a character may map to itself.
 * 
 * 
 * Example 1:
 * Input: s = "egg", t = "add"
 * Output: true
 * Example 2:
 * Input: s = "foo", t = "bar"
 * Output: false
 * Example 3:
 * Input: s = "paper", t = "title"
 * Output: true
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 5 * 10^4
 * t.length == s.length
 * s and t consist of any valid ascii character.
 * 
 * 
 */

// @lc code=start
class Solution {
    public boolean isIsomorphic(String s, String t) {
        return usingHashMaps(s, t);
    }

    private boolean usingHashMaps(String s, String t) {
        if(s.length() != t.length()) return false;
        HashMap<Character, Character> st = new HashMap<>();
        HashMap<Character, Character> ts = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if ((!st.containsKey(s.charAt(i)) && ts.containsKey(t.charAt(i)))) {
                return false;
            }
            if (st.containsKey(s.charAt(i)) && ts.containsKey(t.charAt(i)) && s.charAt(i) != ts.get(t.charAt(i))) {
                return false;
            }
            if (st.containsKey(s.charAt(i)) && t.charAt(i) != st.get(s.charAt(i))) {
                return false;
            }
            st.put(s.charAt(i), t.charAt(i));
            ts.put(t.charAt(i), s.charAt(i));
            st.containsValue(ts);
        }
        return true;
    }
}
// @lc code=end

