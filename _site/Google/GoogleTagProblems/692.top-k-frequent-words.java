/*
 * @lc app=leetcode id=692 lang=java
 *
 * [692] Top K Frequent Words
 *
 * https://leetcode.com/problems/top-k-frequent-words/description/
 *
 * algorithms
 * Medium (53.93%)
 * Likes:    6605
 * Dislikes: 309
 * Total Accepted:    515.9K
 * Total Submissions: 906K
 * Testcase Example:  '["i","love","leetcode","i","love","coding"]\n2'
 *
 * Given an array of strings words and an integer k, return the k most frequent
 * strings.
 *
 * Return the answer sorted by the frequency from highest to lowest. Sort the
 * words with the same frequency by their lexicographical order.
 *
 *
 * Example 1:
 *
 *
 * Input: words = ["i","love","leetcode","i","love","coding"], k = 2
 * Output: ["i","love"]
 * Explanation: "i" and "love" are the two most frequent words.
 * Note that "i" comes before "love" due to a lower alphabetical order.
 *
 *
 * Example 2:
 *
 *
 * Input: words =
 * ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
 * Output: ["the","is","sunny","day"]
 * Explanation: "the", "is", "sunny" and "day" are the four most frequent
 * words, with the number of occurrence being 4, 3, 2 and 1 respectively.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= words.length <= 500
 * 1 <= words[i].length <= 10
 * words[i] consists of lowercase English letters.
 * k is in the range [1, The number of unique words[i]]
 *
 *
 *
 * Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
 *
 */

import java.util.*;

// @lc code=start
class Solution {

  class Pair {
    String word;
    int count;

    Pair(String word, int count) {
      this.word = word;
      this.count = count;
    }
  }

  public List<String> topKFrequent(String[] words, int k) {
    HashMap<String, Integer> map = new HashMap<>();
    for (var word : words) {
      map.put(word, map.getOrDefault(word, 0) + 1);
    }
    PriorityQueue<Pair> pq = new PriorityQueue<>(
      (p1, p2) -> {
        if (p1.count == p2.count) {
          return p1.word.compareTo(p2.word);
        }
        return Integer.compare(p2.count, p1.count);
      }
    );
    map.forEach(
      (word, count) -> {
        pq.add(new Pair(word, count));
      }
    );
    LinkedList<String> result = new LinkedList<String>();
    while (k-- > 0) {
      result.add(pq.poll().word);
    }
    return result;
  }
}
// @lc code=end
