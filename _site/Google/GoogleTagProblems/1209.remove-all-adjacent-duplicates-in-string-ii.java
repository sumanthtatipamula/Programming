package Google.GoogleTagProblems;

/*
 * @lc app=leetcode id=1209 lang=java
 *
 * [1209] Remove All Adjacent Duplicates in String II
 *
 * https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/
 *
 * algorithms
 * Medium (56.13%)
 * Likes:    4862
 * Dislikes: 90
 * Total Accepted:    253.6K
 * Total Submissions: 452.7K
 * Testcase Example:  '"abcd"\n2'
 *
 * You are given a string s and an integer k, a k duplicate removal consists of
 * choosing k adjacent and equal letters from s and removing them, causing the
 * left and the right side of the deleted substring to concatenate together.
 *
 * We repeatedly make k duplicate removals on s until we no longer can.
 *
 * Return the final string after all such duplicate removals have been made. It
 * is guaranteed that the answer is unique.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "abcd", k = 2
 * Output: "abcd"
 * Explanation: There's nothing to delete.
 *
 * Example 2:
 *
 *
 * Input: s = "deeedbbcccbdaa", k = 3
 * Output: "aa"
 * Explanation:
 * First delete "eee" and "ccc", get "ddbbbdaa"
 * Then delete "bbb", get "dddaa"
 * Finally delete "ddd", get "aa"
 *
 * Example 3:
 *
 *
 * Input: s = "pbbcggttciiippooaais", k = 2
 * Output: "ps"
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 10^5
 * 2 <= k <= 10^4
 * s only contains lowercase English letters.
 *
 *
 */

// @lc code=start
class Solution {

  class Pair {
    char letter;
    int count;

    Pair(char letter, int count) {
      this.letter = letter;
      this.count = count;
    }
  }

  public String removeDuplicates(String s, int k) {
    Stack<Pair> st = new Stack<>();
    for (char c : s.toCharArray()) {
      if (st.isEmpty() || st.peek().letter != c) {
        st.push(new Pair(c, 1));
      } else {
        st.peek().count += 1;
      }
      if (st.peek().count == k) {
        st.pop();
      }
    }
    StringBuffer sb = new StringBuffer();
    while (!st.isEmpty()) {
      var p = st.pop();
      for (int i = 0; i < p.count; i++) {
        sb.append(p.letter);
      }
    }
    return sb.reverse().toString();
  }
}
// @lc code=end
