import java.util.Stack;

/*
 * @lc app=leetcode id=20 lang=java
 *
 * [20] Valid Parentheses
 *
 * https://leetcode.com/problems/valid-parentheses/description/
 *
 * algorithms
 * Easy (40.34%)
 * Likes:    9010
 * Dislikes: 355
 * Total Accepted:    1.6M
 * Total Submissions: 4.1M
 * Testcase Example:  '"()"'
 *
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and
 * ']', determine if the input string is valid.
 * 
 * An input string is valid if:
 * 
 * 
 * Open brackets must be closed by the same type of brackets.
 * Open brackets must be closed in the correct order.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "()"
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "()[]{}"
 * Output: true
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "(]"
 * Output: false
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: s = "([)]"
 * Output: false
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: s = "{[]}"
 * Output: true
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 10^4
 * s consists of parentheses only '()[]{}'.
 * 
 * 
 */

// @lc code=start
class Solution {
    private char returnOpenBrace(char closed) {
        if (closed == ')')
            return '(';
        if (closed == '}')
            return '{';
        return '[';
    }
    
    private boolean isOpenBrace(char brace) {
        return brace == '{' || brace == '[' || brace == '(';
    }

    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
        for (var i = 0; i < s.length(); i++) {
            if (isOpenBrace(s.charAt(i))) {
                st.push(s.charAt(i));
            }
            else if (st.isEmpty() || st.peek() != returnOpenBrace(s.charAt(i))) {
                return false;
            }
            else {
                st.pop();
            }
        }
        return st.isEmpty();
    }
}
// @lc code=end

